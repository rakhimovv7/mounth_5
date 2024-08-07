from django.shortcuts import render
from apps.todolist.models import *
from apps.todolist.serialzers import *
# Create your views here.
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TaskSerializer
