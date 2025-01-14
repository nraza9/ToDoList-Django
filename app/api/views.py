from ..models import Task
from .serializers import AppSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# REST API request handers

class AppViewSet(APIView):
  
    serializer_class = AppSerializer

    def get(self, request):
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

    #ToDo: add code    
    def patch(self, request, task_id=None):
        return  Response(request.data)
