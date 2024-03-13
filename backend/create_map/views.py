from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

import json
from datetime import datetime, timedelta
import time
from create_map.models import Project,Task,Comment
from accounts.models import UserAccount


# from .task import my_scheduled_task
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks(request):
   
    tasks=Task.objects.all()

    # for i in range(10):
    tasks_data=[]
    for task in tasks:
        task_data={}
        task_data['id']=task.id
        task_data['assignee']=task.assignee.username
        task_data['creator']=task.creator.username
        task_data['reportor']=task.reportor.username
        task_data['name']=task.name
        task_data['description']=task.description
        task_data['notes']=task.notes
        task_data['state']=task.state
        task_data['priority']=task.priority
        task_data['start_date']=task.start_date
        task_data['due_date']=task.due_date
        task_data['create_at']=task.create_at
        tasks_data.append(task_data)
        
    return Response(tasks_data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_projects(request):
   
    projects=Project.objects.all()

    # for i in range(10):
    projects_data=[]
    for project in projects:
        project_data={}
        project_data['id']=project.id
        project_data['name']=project.name
        project_data['description']=project.description
        project_data['state']=project.state
        project_data['start_date']=project.start_date
        project_data['due_date']=project.due_date
        project_data['create_at']=project.create_at
        projects_data.append(project_data)
        
    return Response(projects_data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comments(request):
   
    comments=Comment.objects.filter(task=request.GET.get('task_id'))
    # for i in range(10):
    comments_data=[]
    for comment in comments:
        comment_data={}
        comment_data['id']=comment.id
        comment_data['creator']=comment.creator.username
        comment_data['message']=comment.message
        comment_data['create_at']=comment.create_at
        comments_data.append(comment_data)
        
    return Response(comments_data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    body = json.loads(request.body)
    proejct=Project()
    proejct.user=UserAccount.objects.filter(id=request.user.id).first()
    proejct.name = body['name']
    proejct.description=body['description']
    proejct.state=body['state']
    proejct.start_date= body['start_date']
    proejct.due_date= body['due_date']
    proejct.create_at= datetime.now()


    proejct.save()
  
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    body = json.loads(request.body)
    task=Task()
    task.creator=UserAccount.objects.get(id=request.user.id)
    task.assignee=UserAccount.objects.get(id=body['assignee']) #assignee id
    task.reportor=UserAccount.objects.get(id=body['assignee']) #assignee id

    task.name = body['name']
    task.description=body['description']
    task.state=body['state']
    task.start_date= body['start_date']
    task.due_date= body['due_date']
    task.create_at= datetime.now()
    task.project = Project.objects.get(id=body['project_id'])

    task.save()
  
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request):
    body = json.loads(request.body)

    comment=Comment()
    comment.task = Task.objects.get(id=body['task_id'])
    comment.creator=UserAccount.objects.get(id=request.user.id)
    comment.message = body['message']
    comment.create_at= datetime.now()


    comment.save()
  
    return Response(status=status.HTTP_201_CREATED)