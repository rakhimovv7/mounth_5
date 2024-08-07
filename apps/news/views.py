from django.shortcuts import render
from apps.news.models import *
from apps.news.serializers import *
# Create your views here.

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView


class NewsCreatedAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    

class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer

class NewsDestroyAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    
class NewsUpdateAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
