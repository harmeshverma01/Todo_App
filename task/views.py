from task.serializers import TaskSerializer

from app.utils import  manager_required
from .models import Task

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from app.models import User

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
            return Response(serializer.errors)
    
    def delete(self, request, id=None):
        task = Task.objects.get(id=id)
        task.delete()
        return Response({'message':'task should be deleted'}, status=status.HTTP_200_OK)
            

class TaskdetailsView(APIView):
    serializer_class = TaskSerializer
    
    def get(self, request, id=None):
        task = Task.objects.all()
        serializer = self.serializer_class(task, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, id=None):
        try:
            task = Task.objects.get(id=id)
            serializer = self.serializer_class(task, data=request.data)
            return Response(serializer.data)
        except:
            return Response(({'details': 'task Not Found'}), status=status.HTTP_404_NOT_FOUND)    
                                
    def patch(self, request, id=None):
        try:
            task = Task.objects.get(id=id)
            serializer = self.serializer_class(task, data=request.data, partial=True)
            return Response(serializer.data)
        except:
            return Response(({'details': 'task not found'}), status=status.HTTP_404_NOT_FOUND)
        
        
    def delete(self, request, id=None):
        task = Task.objects.get(id=id)
        task.delete()
        return Response(({'message': 'task is deleted'}), status=status.HTTP_204_NO_CONTENT)            



class TaskcharaterView(APIView):
    serializer_class = TaskSerializer
    
    def get(self, request, id=None):
        user = User.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, id=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def put(self, request, id=None):
        try:
            user = User.objects.get(id=id)
            serializer = self.serializer_class(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except:
            return Response(({'detaisl': 'user not found'}), status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, id=None):
        try:
            user = User.objects.get(id=id)
            serializer = self.serializer_class(user, data=request.data, partial=True)
            return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
        except:
            return Response(({'details', 'user not found'}), status=status.HTTP_204_NO_CONTENT)
        
    def delete(self, request, id=None):
        user = User.objects.get(id=id)
        user.delete()
        return Response(({'message': 'user is deleted'}), status=status.HTTP_204_NO_CONTENT)



class Requiretask(APIView):
    serializer_class = TaskSerializer
    
    def get(self, request, id=None):
        task = Task.objects.all()
        serializer = self.serializer_class(task)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors)
        return Response(serializer.data)
    
    def patch(self, request, id=None):
        try:
            task = Task.objects.get(id=id)
            serializer = self.serializer_class(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.errors)
            return Response(serializer.data)
        except:
            return Response(({'message': 'task not found'}), status=status.HTTP_404_NOT_FOUND)
        
    def  delete(self, request, id=None):
        task = Task.object.get(id=id)
        task.delete()
        return Response(({'details': 'task is deleted'}), status=status.HTTP_204_NO_CONTENT)       
    
    
class SawstatusView(APIView):
    serializer_class = TaskSerializer
    
    def get(self, request, id=None):
        task = Task.objects.all()
        serializer = self.serializer_class(task)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def patch(self, request, id=None):
        try:
            task = Task.objects.get(id=id)
            serializer = self.serializer_class(task, data=request.data, partial=True)
            return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
        except:
            return Response(({'message' : 'task is invalid'}), status=status.HTTP_204_NO_CONTENT)
        
    def delete(self, request, id=None):
        task = Task.objects.get(id=id)
        task.delete()
        return Response(({'message' : 'task is deleted successfully'}), status=status.HTTP_204_NO_CONTENT)
          