from django.shortcuts import render
from app.serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
# Create your views here.

class Userview(APIView):
    serializers_classes = UserSerializer
    queryset = User.objects.all()
    
    def get(self, request, pk=None):
        user = User.objects.all()
        serializer= UserSerializer(user)
        return Response(serializer.data)
        
    
    def post(self, request):
        pass
    
    def put(request):
        pass
    
    def patch(self, request):
        pass
    
    def delete():
        pass
        