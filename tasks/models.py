from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)  # Task title
    description = models.TextField()           # Task description
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])  # Task status
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # User assigned to the task
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for task creation

    def __str__(self):
        return self.title 