from rest_framework import serializers

from .models import TodoList

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['title','description','completed','created']