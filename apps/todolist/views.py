from django.shortcuts import render
from apps.todolist.models import *
from apps.todolist.serialzers import *
# Create your views here.

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

class TaskAPI(GenericViewSet, 
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              ):
    queryset = TodoList.objects.all()
    serializer_class = TaskSerializer