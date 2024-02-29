from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import json
from datetime import datetime, timedelta
import time



# from .task import my_scheduled_task
@api_view(['GET'])
def testing(request):
   
    task=[]

    # for i in range(10):
    sensorData={}
    sensorData['id']=1
    sensorData['id_name']="task"
    sensorData['description']="testing123"
        
    task.append(sensorData)
    return Response(task)

