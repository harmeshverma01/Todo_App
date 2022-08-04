from app.serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from . import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import authentication
# Create your views here.

class Userview(APIView):
    serializer_class = UserSerializer
    
    
    def get(self, request, id=None):
        #its for user id 
        if id:
            try:
                user = User.objects.get(id=id)
                serializer = self.serializer_class(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response({'details': 'does not found'}, status=status.HTTP_404_NOT_FOUND)
        #its for user list
        else:
            user = User.objects.all()
            serializer = self.serializer_class(user, many=True)
            return Response(serializer.data)
                    
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"massage" : "Details Not found"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
    
    def put(self, request, id=id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "Details does not found"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    
    
    
    def patch(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "Details does not found"}, status=status.HTTP_404_NOT_FOUND)
                
                
    def delete(self, request, id):
        user = User.objects.get(id)
        serializer = self.serializer_class(user)
        user.delete()
        return Response({"message": "User is deleted"}, status=status.HTTP_400_BAD_REQUEST)            
     
    
 
 
class Loginview(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user:
            token = Token.objects.get_or_create(user=user)
            print("NNJNMUNUMU", token)
            return Response({'token': str(token[0])})
        return Response({'details': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
     