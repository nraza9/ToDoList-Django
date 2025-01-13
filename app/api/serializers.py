from rest_framework.serializers import ModelSerializer
from ..models import Task 

class AppSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at')
        