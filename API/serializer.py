from rest_framework import serializers
from .models import Emp

class EmpSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    e_id=serializers.IntegerField()
    salary=serializers.IntegerField()
