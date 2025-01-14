from ..models import Task
from .serializers import AppSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# REST API request handers
class AppViewSet(APIView):
  
    serializer_class = AppSerializer

    def get(self, request, task_id=None):
        # Get the single task
        if task_id != None:
            task = get_object_or_404(Task, pk=task_id)
            data = {
                'id': task.id,
                'title': task.title,
            }
            return Response(data)
        
        # Return all tasks
        # Data to be returned
        detail = [ {"id": detail.id, "title": detail.title, "created": detail.created_at} 
        for detail in Task.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = AppSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)
    
    # DELETE method for deleting a task by ID
    def delete(self, request, task_id=None):
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return Response({"message": "Task deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

    # Update the Task's title   
    def patch(self, request, task_id=None):
        try:
            item = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AppSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
