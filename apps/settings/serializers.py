from rest_framework import serializers

from .models import Settings


class SettingtsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['title','description']

class SettingtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'
        
        

        
