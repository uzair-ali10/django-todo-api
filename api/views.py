from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Task
import datetime
from rest_framework import status
from rest_framework.response import Response
from .serializers import TaskSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def get_all_tasks(request):
    body_data = request.data

    if request.method == 'GET':
        data = Task.objects.all()
        serialized_data = TaskSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serialized_data = TaskSerializer(data=body_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_todos(request):
    data = Task.objects.all().filter(is_completed=False)
    serialized_data = TaskSerializer(data, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
def complete_task(request, pk):
    body_data = request.data

    try:
        req_task = Task.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        serialized_task = TaskSerializer(req_task, data=body_data)
        if serialized_task.is_valid():
            serialized_task.save()
            return Response(serialized_task.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialized_task.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        req_task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)