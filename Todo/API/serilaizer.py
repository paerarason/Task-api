from rest_framework import serializers
from .models import Task

'''     
Task Serializer that handle the task object to Api format Json,XML etc...
'''
class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'