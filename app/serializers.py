from dataclasses import fields
from rest_framework import serializers
from app.manager import UserManager
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'email', 'role', 'password']
        model =  User
    

