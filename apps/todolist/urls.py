from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

rout = DefaultRouter()
rout.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(rout.urls)),
]
