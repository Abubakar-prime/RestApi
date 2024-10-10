from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()  # Retrieve all tasks
    serializer_class = TaskSerializer  # Use the TaskSerializer for the response

class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()  # Retrieve tasks by primary key
    serializer_class = TaskSerializer  # Use the TaskSerializer for the response
