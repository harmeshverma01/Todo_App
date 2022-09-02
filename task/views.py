from functools import partial
from urllib import response
from task.serializers import TaskSerializer
from rest_framework.response import Response
from app.utils import  manager_required
from .models import Task
from rest_framework.views import APIView
from rest_framework import status



class TaskView(APIView):
    
    serializer_class = TaskSerializer
    permission_classes = [manager_required]
    
    def get(self, request, id=None):
        task = Task.objects.all()
        completed = request.GET.get('completed', None)
        if task is not None:
            task = task.filter(completed=completed)
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



class UserResultView():
    serializer_class  = TaskSerializer
        
    def get(self, request):
        task = Task.objects.get()
        serializer = self.serializer_class(task, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        task = Task.objects.create(
            title = request.get('title'),
            discreption = request.get('discreption'),
            completed = request.get('completed'),
            object = request.get('object'),
        )
        task.save()
        serializer = self.serializer_class()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
            
    def patch(self, request, id=None):
        try:
            task = Task.objects.get(id=id)
            serializer = self.serializer_class(task, data=request.data ,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Task.DoesNotExist:
            return response(serializer.errors)
    
    def delete(self, request, id=None):
        task = Task.objects.get(id=id)
        task.delete()
        return Response({'message':'task should be deleted'}, status=status.HTTP_200_OK)
            
                        
            
             