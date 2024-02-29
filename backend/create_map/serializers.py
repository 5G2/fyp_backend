from rest_framework.serializers import ModelSerializer
from create_map.models import Sensor, Sign, Wire, Branch,Alerts,Floor

class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor 
        fields = '__all__'

class SignSerializer(ModelSerializer):
    class Meta:
        model = Sign 
        fields = '__all__'

class WireSerializer(ModelSerializer):
    class Meta:
        model = Wire
        fields = '__all__'

class BranchSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class AlertSerializer(ModelSerializer):
    class Meta:
        model = Alerts
        fields = '__all__'

class FloorSerializer(ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'