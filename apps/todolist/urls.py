from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskAPI

rout = DefaultRouter()
rout.register(r'tasks', TaskAPI)

urlpatterns = [
    path('', include(rout.urls)),
]
