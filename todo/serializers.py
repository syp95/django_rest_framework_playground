from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['id','title','complete','important']

class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['id','title','description','complete','important']