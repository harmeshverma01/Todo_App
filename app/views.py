import email
from functools import partial
from unicodedata import name
from django.shortcuts import render
from app.serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from . import serializers
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class Userview(APIView):
    serializer_class = UserSerializer
    
    
    def get(self, request, id=None):
        if id:
            try:
                user = User.objects.get(id=id)
                serializer = self.serializer_class(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response({'details': 'does not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            user = User.objects.all()
            serializer = self.serializer_class(user, many=True)
            return Response(serializer.data)
                    
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # name = serializer.validated_data.get("name")
            # email = serializer.validated_data.get("email")
            # role = serializer.validated_data.get("role")
            # date = serializer.validated_data.get ("date")
            serializer.save()
            # user.objects.create(
            #     name = name,
            #     email = email,
            #     role = role, 
            #     date = date
            # )
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"massage" : "Details Not found"}, status=status.HTTP_404_NOT_FOUND)
            
    
    def put(self, request, id=id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "Details does not found"})
        
    
    def patch(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "Details does not found"})
                
        
    
    def delete(self, request, id):
        user = User.objects.get()
        user.delete()
        return Response({"message": "User is deleted"})
        