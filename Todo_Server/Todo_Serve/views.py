from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def set_completed(self, request, pk=None):
        task = self.get_object()
        task.completed = request.data.get('completed', task.completed)
        task.save()
        return Response(TaskSerializer(task).data)