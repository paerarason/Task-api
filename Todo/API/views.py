from django.shortcuts import render,HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.decorators import api_view
from django.contrib.auth.models import User,Group
from .models import Task
from rest_framework.views import APIView
from rest_framework import viewsets
from .serilaizer import Taskserializer


'''
List the All Task 
'''


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class =Taskserializer


'''
Particular Task GET ,PUT ,DELETE 
'''
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = Taskserializer