from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from .models import Settings
from .serializers import *

class SettingsAPIView(ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingtsSerializer
    
class SettingsAPICreate(CreateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingtsCreateSerializer
    
class SettingsAPIRetrieve(RetrieveAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingtsCreateSerializer

class SettingsAPIUpdate(UpdateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingtsCreateSerializer

class SettingsAPIDestroy(DestroyAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingtsCreateSerializer
    
    