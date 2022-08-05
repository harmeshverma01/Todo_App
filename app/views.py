from functools import partial
from app.serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import authentication, permissions
from django.shortcuts import get_object_or_404
from .utils import admin_required, manager_required


class Userview(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated, admin_required, manager_required]
    serializer_class = UserSerializer
    
    
    
    def get(self, request, id=None):
        if id:
            try:
                user = get_object_or_404(User, id)
                serializer = self.serializer_class(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response({'details': 'does not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            user = User.objects.filter()
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
    
    
    
    
    def patch(self, request, id=None):
        try:
            user = User.objects.update(
                name = request.data.get('name'),
                email = request.data.get('email'),
                password = request.data.get('password'),
                role = request.data.get('role')
            )
            #user = User.objects.get(id)
            serializer = UserSerializer(user,data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except:
            return Response({"message": "Details does not found"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        # user = User.objects.update()
        # #user = User.objects.get(id=id)
        # serializer = UserSerializer(user, data=request.data, partial=True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response({"message": "Details does not found"}, status=status.HTTP_404_NOT_FOUND)
                
                
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
     

class UserDetailsView(APIView):
    serializer_class = UserSerializer
    
    def get(self, request, id=None):
            user = User.objects.filter()
            serializer = self.serializer_class(user, many=True)
            return Response(serializer.data)
    
        
    