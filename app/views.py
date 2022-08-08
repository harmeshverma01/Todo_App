from app.serializers import UserSerializer, TaskSerializer
from rest_framework import authentication, permissions
from .utils import admin_required, manager_required
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .models import User, Assign, Task
from rest_framework import status
from functools import partial
from app import serializers



class Userview(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated, admin_required, manager_required]
    serializer_class = UserSerializer
    
    
    
    def get(self, request, id=None):
        user = User.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
                    
    
    def post(self, request):
        user = User.objects.create_user(
            name = request.data.get('name'),
            email = request.data.get('email'),
            password = request.data.get('password'),
            role = request.data.get('role', 'User')
        )
        serializer =  UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
    
    # def put(self, request, id=None):
    #     try:
            
    #         user = User.objects.update(
    #             name = request.data.get('name'),
    #             email = request.data.get('email'),
    #             password = request.data.get('password'),
    #             role = request.data.get('role')
    #         )
    #         #user = User.objects.get(id)
    #         serializer = UserSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #         return Response(serializer.data)
            
    #     except:
    #         return Response({"message": "Details does not found"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    
    
    
    # def patch(self, request, id=None):
    #     #user = User.objects.get(id)
    #     serializer = UserSerializer(user,data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)
        
        
        # user = User.objects.update()
        # #user = User.objects.get(id=id)
        # serializer = UserSerializer(user, data=request.data, partial=True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response({"message": "Details does not found"}, status=status.HTTP_404_NOT_FOUND)
                
                
    def delete(self, request, id=None):
        user = User.objects.get(id=id)
        serializer = self.serializer_class(user, data=request.data)
        user.delete()
        return Response({"message": "User is deleted"}, status=status.HTTP_204_NO_CONTENT)            
        
class Loginview(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'token': str(token[0])})
        return Response({'details': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
     

class UserDetailsView(APIView):
    serializer_class = UserSerializer
    peermission_classes = [admin_required]
    
    def get(self, request, id=None):
            user = User.objects.get(id=id)
            serializer = self.serializer_class(user)
            return Response(serializer.data)
    
    def patch(self, request, id=None):
        try:
            user = User.objects.get(id=id)
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id=None):
       user = User.objects.get(id=id)
       user.delete()
       return Response(({"message": "User is deleted"}),status=status.HTTP_204_NO_CONTENT)     
        

class TasKView(APIView):
    
    serializer_class = TaskSerializer
    permission_classes = [manager_required]
    
    def get(self, request, id=None):
        task = Task.objects.all()
        serializers = self.serializer_class(task, many=True)
        return Response(serializers.data)
        
    def post(self, request,):
        task = Task.objects.create(
            title  = request.data.get("title"),
            discription = request.data.get("discription")
            )
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    
    def patch(self, request, id=None):
        try:
            task = Task.objects.get(id=id)
            serializers = self.serializer_class(task, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
        except Task.DoesNotExist:
            return Response(({'message': 'Details Not Found'}), status=status.HTTP_404_NOT_FOUND)    
               
               
    def delete(self, request, id=None):
        task = Task.objects.get(id=id)
        task.delete()
        return Response(({'message': 'Task Deleted sucessfully'}), status=status.HTTP_204_NO_CONTENT)           
    
    