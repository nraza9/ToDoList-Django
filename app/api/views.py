from rest_framework.viewsets import ModelViewSet
from ..models import Task
from .serializers import AppSerializer

from django.shortcuts import render
from rest_framework.views import APIView
#from . models import *
from rest_framework.response import Response
#from . serializer import *
from rest_framework import status

# class AppViewSet(ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = AppSerializer
    
class AppViewSet(APIView):
  
    serializer_class = AppSerializer

    def get(self, request):
        # Data to be returned
        detail = [ {"id": detail.id, "title": detail.title, "created": detail.created_at} 
        for detail in Task.objects.all()]
        return Response(detail)

    def post(self, request):
        print('=== post')
        serializer = AppSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)
    
    # DELETE method for deleting a task by ID
    def delete(self, request, task_id=None):
        print("=== delete: " + str(task_id))
        #print("=== request: " + str(request.data['id']))
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return Response({"message": "Task deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, task_id=None):
        print("=== patch: " )
        return  Response(request.data)
