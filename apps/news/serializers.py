from rest_framework import serializers

from .models import News


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title','description','photo','create_data']

        
        

        
