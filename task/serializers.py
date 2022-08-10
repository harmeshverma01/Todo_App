from rest_framework import serializers
from app.manager import UserManager
from .models import  Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'