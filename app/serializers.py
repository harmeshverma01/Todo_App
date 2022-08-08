from rest_framework import serializers
from app.manager import UserManager
from .models import Assign, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'email', 'role', 'password']
        model =  User
    

class AssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assign
        fields = '__all__'