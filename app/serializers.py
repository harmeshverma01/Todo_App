from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'email', 'role', 'date']
        model = User
        
      