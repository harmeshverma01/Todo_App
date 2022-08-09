from app.serializers import UserSerializer, AssignSerializer
from rest_framework import authentication, permissions
from .utils import admin_required, manager_required
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .models import User, Assign
from rest_framework import status
from rest_framework import filters
from django.shortcuts import render


#User APIs
class Userview(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated, admin_required, manager_required]
    serializer_class = UserSerializer
    
    
    
    
    def get(self, request, id=None):
        user = User.objects.all()
        role = request.GET.get('role', None)
        if role is not None:
            user = user.filter(role=role)
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
       
                
                
        
#Login APIs        
class Loginview(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'token': str(token[0])})
        return Response({'details': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
     

#UserDetails APIs
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
        


#ManagerView APIs
class ManagerView(APIView):
    serializer_class = UserSerializer
    permission_classes = [admin_required]
    
    def get(self, request, id=None):
        user = User.objects.filter(role="Manager")
        serializers = self.serializer_class(user)
        return Response(serializers.data)

#AssignView        
class AssignUserView(APIView):
    serializer_class = AssignSerializer
    permission_classes = [admin_required]
    
    def get(self, request, id=None):
        user = Assign.objects.get()
        serializers = self.serializer_class(user)
        return Response(serializers.data)
    
    def post(self, request):
        user = Assign.objects.create(
            user = request.data.get("user"),
            manager = request.data.get("manager")
            )
        serializers = AssignSerializer(user)
        return Response(serializers.data, status=status.HTTP_201_CREATED)
        
    def patch(self, request, id=None):
        user = Assign.objects.get(id=id)
        serializers = self.serializer_class(user, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data) 
        
        
def getuser(request):
    User.objects.all()
    return render(request, "app/index.html", {})


        
        