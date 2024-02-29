from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import csv
import time
import tkinter as tk
from tkinter import ttk


current_state = 'bothok'
manual_mode = False

class Sensor:
    temperature = "0"
    smoke = "0"

    
class TemperatureHandler(SimpleHTTPRequestHandler, Sensor):
    sensor1 = Sensor()
    sensor2 = Sensor()
    sensor3 = Sensor()
    sensor4 = Sensor()
    state = "bothok"
    def do_POST(self):
    
        # Read temperature from POST data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        if post_data.split(",")[0] == "1":
            self.sensor1.temperature = post_data.split(",")[1]
            self.sensor1.smoke = str(round((float(post_data.split(",")[2])%1000) / 10.24 , 2))
            print("\nReceived from Sensor1 | Temperature: " + self.sensor1.temperature + " | Smoke Level: "+ self.sensor1.smoke + "\n")
            with open("sensor_data.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([time.ctime(time.time()),post_data.split(",")[0], self.sensor1.temperature, self.sensor1.smoke])
        elif post_data.split(",")[0] == "2":
            self.sensor2.temperature = post_data.split(",")[1]
            self.sensor2.smoke = str(round((float(post_data.split(",")[2])%1000) / 10.24 , 2))
            print("\nReceived from Sensor2 | Temperature: " + self.sensor2.temperature + " | Smoke Level: "+ self.sensor2.smoke + "\n")
            with open("sensor_data.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([time.ctime(time.time()),post_data.split(",")[0], self.sensor2.temperature, self.sensor2.smoke])
        elif post_data.split(",")[0] == "3":
            self.sensor3.temperature = post_data.split(",")[1]
            self.sensor3.smoke = str(round((float(post_data.split(",")[2])%1000) / 10.24 , 2))
            print("\nReceived from Sensor3 | Temperature: " + self.sensor3.temperature + " | Smoke Level: "+ self.sensor3.smoke + "\n")
            with open("sensor_data.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([time.ctime(time.time()),post_data.split(",")[0], self.sensor3.temperature, self.sensor3.smoke])
        elif post_data.split(",")[0] == "4":
            self.sensor4.temperature = post_data.split(",")[1]
            self.sensor4.smoke = str(round((float(post_data.split(",")[2])%1000) / 10.24 , 2))
            print("\nReceived from Sensor4 | Temperature: " + self.sensor4.temperature + " | Smoke Level: "+ self.sensor4.smoke + "\n")
            with open("sensor_data.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([time.ctime(time.time()),post_data.split(",")[0], self.sensor4.temperature, self.sensor4.smoke])
        
        
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        global current_state
        self.state = current_state
        left = False
        right = False
        if float(self.sensor1.temperature) > 31 or float(self.sensor1.smoke) > 70:
            left = True
        if float(self.sensor2.temperature) > 31 or float(self.sensor2.smoke) > 70:
            right = True
            
        if left&right:
            self.state = "return"
        elif left:
            self.state = "left"
        elif right:
            self.state = "right"
            
        if not manual_mode:
            current_state = self.state
            
        jdata = {"sensor1":{"temperature":self.sensor1.temperature,"smoke":self.sensor1.smoke},
                 "sensor2":{"temperature":self.sensor2.temperature,"smoke":self.sensor2.smoke},
                 "sensor3":{"temperature":self.sensor3.temperature,"smoke":self.sensor3.smoke},
                 "sensor4":{"temperature":self.sensor4.temperature,"smoke":self.sensor4.smoke},
                 "state":current_state}
        
        
        json_data = json.dumps(jdata)
        # Send current state
        self.send_response(200)
        # self.send_header("Content-Type", "application/json")
        # self.send_header("Content-Length", len(json_data))
        # self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(json_data.encode())
        # print("SENDING: ",json.dumps(jdata))


# Create a function to update the GUI with new sensor data
def update_gui():
    # temperature_var.set(f"Temperature: {temp} °C")
    # smoke_var.set(f"Smoke Level: {smoke}")
    # sensor1_var.set(f"Sensor 1: {sensor1}")
    # sensor2_var.set(f"Sensor 2: {sensor2}")
    # sensor3_var.set(f"Sensor 3: {sensor3}")
    # sensor4_var.set(f"Sensor 4: {sensor4}")
    state_var.set(f"State: {current_state}")
    root.update_idletasks()

def update_gui_and_server():
    global root, httpd

    # Call your update_gui function here with the required arguments
    update_gui()

    # Update the server
    httpd.handle_request()

    # Schedule the next update
    root.after(100, update_gui_and_server)
    
def toggle_mode():
    global manual_mode
    manual_mode = not manual_mode
    mode_button_text.set("Manual" if manual_mode else "Sensor")

def manual_state_change(new_state):
    global current_state, manual_mode
    if manual_mode:
        current_state = new_state


# Initialize the tkinter GUI
root = tk.Tk()
root.title("Sensor Data")

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 16), background="#FFFFFF")
style.configure("TFrame", background="#FFFFFF")

frame = ttk.Frame(root)
frame.pack(expand=True, fill="both", padx=20, pady=20)

temperature_var = tk.StringVar()
smoke_var = tk.StringVar()
sensor1_var = tk.StringVar()
sensor2_var = tk.StringVar()
sensor3_var = tk.StringVar()
sensor4_var = tk.StringVar()
state_var = tk.StringVar()

temperature_label = ttk.Label(frame, textvariable=temperature_var)
smoke_label = ttk.Label(frame, textvariable=smoke_var)
sensor1_label = ttk.Label(frame, textvariable=sensor1_var)
sensor2_label = ttk.Label(frame, textvariable=sensor2_var)
sensor3_label = ttk.Label(frame, textvariable=sensor3_var)
sensor4_label = ttk.Label(frame, textvariable=sensor4_var)
state_label = ttk.Label(frame, textvariable=state_var)

# temperature_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
# smoke_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
# sensor1_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
# sensor2_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
# sensor3_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
# sensor4_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
state_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

root.configure(bg="#FFFFFF")

mode_button_text = tk.StringVar()
mode_button_text.set("Sensor")
mode_button = ttk.Button(frame, textvariable=mode_button_text, command=toggle_mode)
mode_button.grid(row=0, column=1, padx=10, pady=10)

left_button = ttk.Button(frame, text="Left", command=lambda: manual_state_change("left"))
left_button.grid(row=1, column=1, padx=10, pady=10)

right_button = ttk.Button(frame, text="Right", command=lambda: manual_state_change("right"))
right_button.grid(row=2, column=1, padx=10, pady=10)

bothok_button = ttk.Button(frame, text="Both OK", command=lambda: manual_state_change("bothok"))
bothok_button.grid(row=3, column=1, padx=10, pady=10)

return_button = ttk.Button(frame, text="Return", command=lambda: manual_state_change("return"))
return_button.grid(row=4, column=1, padx=10, pady=10)

# Run the server in the main thread
server_address = ('', 80)
httpd = ThreadingHTTPServer(server_address, TemperatureHandler)
print("HTTP server running on port 80")

# Schedule the first update for the GUI and server
root.after(100, update_gui_and_server)

# Start the Tkinter main loop
root.mainloop()
