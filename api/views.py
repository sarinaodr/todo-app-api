from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<int:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<int:pk>/',
        'Delete' : '/task-delete/<int:pk>',
    }
    
    return Response(api_urls)


@api_view(['GET'])
def TaskListApi(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def TaskDetailApi(request , pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task , many=False)
    return Response(serializer.data)


@api_view(['POST'])
def TaskCreateApi(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(['POST'])
def TaskUpdateApi(request , pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task , data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(['DELETE'])
def TaskDeleteApi(request , pk):
    task = Task.objects.get(id=pk)
    task.delete()
    
    return Response('Item succsesfully deleted')