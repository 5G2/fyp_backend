from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from django.db.models import Count, Value
from django.db.models.functions import Coalesce

import json
from datetime import datetime, timedelta
import time
from create_map.models import Project,Task,Comment,Event,PeopleInProject
from accounts.models import UserAccount

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task_count_by_group(request):
    tasks = Task.objects.all()
    request.user.last_login=datetime.now()
    grouped_tasks = (
        tasks.values('project_id', 'project__code')
        .annotate(
            open=Coalesce(Count('id', filter=Q(state=1)), Value(0)),
            inprogress=Coalesce(Count('id', filter=Q(state=2)), Value(0)),
            closed=Coalesce(Count('id', filter=Q(state=3)), Value(0)),
            onhold=Coalesce(Count('id', filter=Q(state=4)), Value(0)),
        )
        .values('project_id', 'project__code', 'open', 'inprogress', 'closed', 'onhold')
    )

    tasks_data = list(grouped_tasks)

    return Response(tasks_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_7days_task(request):
    current_date = datetime.now()
    start_date = current_date
    end_date = current_date + timedelta(days=7)
    privious_date = current_date - timedelta(days=7)

    tasks=Task.objects.filter(Q(assignee=request.user.id)|Q(reportor=request.user.id)|Q(creator=request.user.id))

    if(request.GET.get("project_code")):
        projects = Project.objects.filter(code=request.GET.get("project_code"))
        tasks=Task.objects.filter(project__in=projects)


    due_tasks = tasks.filter(due_date__range=[start_date, end_date])
    number_of_due_tasks=due_tasks.count()

    updated_tasks = tasks.filter(last_update__range=[privious_date, start_date])
    number_of_updated_tasks=updated_tasks.count()

    done_task = tasks.filter(last_update__range=[privious_date, start_date]).filter(state=3)
    number_of_done_task=done_task.count()

    create_task = tasks.filter(create_at__range=[privious_date, start_date])
    number_of_create_task=create_task.count()

    response ={}
    response["number_of_due_tasks"]=number_of_due_tasks
    response["number_of_updated_tasks"]=number_of_updated_tasks
    response["number_of_done_task"]=number_of_done_task
    response["number_of_create_task"]=number_of_create_task
    return Response(response)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_total_task_number(request):
    tasks=Task.objects.filter(Q(assignee=request.user.id)|Q(reportor=request.user.id)|Q(creator=request.user.id))

    open_tasks = tasks.filter(state=1)
    number_of_open_tasks=open_tasks.count()

    closed_tasks = tasks.filter(state=3)
    number_of_closed_tasks=closed_tasks.count()

    in_progress_tasks = tasks.filter(state=2)
    number_of_in_progress_tasks=in_progress_tasks.count()

    on_hold_tasks = tasks.filter(state=4)
    number_of_on_hold_tasks=on_hold_tasks.count()

    response ={}
    response["number_of_open_tasks"]=number_of_open_tasks
    response["number_of_closed_tasks"]=number_of_closed_tasks
    response["number_of_in_progress_tasks"]=number_of_in_progress_tasks
    response["number_of_on_hold_tasks"]=number_of_on_hold_tasks
    return Response(response)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_user(request):
   
    users=UserAccount.objects.all()
        
    users_data=[]
    for user in users:
            
        user_data={}
        user_data['id']=user.id
        user_data['email']=user.email
        user_data['username']=user.username
        user_data['role']=user.role
        user_data['gender']=user.gender
        user_data['phone']=user.phone
        user_data['createAt']=user.create_at
        user_data['lastLogin']=user.last_login
        user_data['birthday']=user.birthday
        user_data['emergencyContact']=user.emergency_contact
        if request.GET.get('project_code'):
            project = Project.objects.filter(code=request.GET.get('project_code')).first()
            if( PeopleInProject.objects.filter(Q(project=project)&Q(user=user)).count()>0):
                user_data['is_project_memeber']=True
            else:
                user_data['is_project_memeber']=False
        users_data.append(user_data)
        
    return Response(users_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_data(request):
   
    users=UserAccount.objects.all()
    user_id=request.GET.get('user_id')
    if(user_id is not None):
        user=UserAccount.objects.get(id=user_id)
    else:
        user=UserAccount.objects.get(id=request.user.id)

    user_data={}
    user_data['id']=user.id
    user_data['email']=user.email
    user_data['username']=user.username
    user_data['role']=user.role
    user_data['gender']=user.gender
    user_data['phone']=user.phone
    user_data['createAt']=user.create_at
    user_data['lastLogin']=user.last_login
    user_data['birthday']=user.birthday
    user_data['emergencyContact']=user.emergency_contact
        
    return Response(user_data)



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_tasks(request):
   
    tasks=Task.objects.all()

    user_id=request.GET.get('user_id')
    if(user_id is not None):
        tasks=Task.objects.filter(Q(assignee=user_id)|Q(reportor=user_id)|Q(creator=user_id))
        
    project_id=request.GET.get('project_id')
    if(project_id is not None):
        tasks=Task.objects.filter(project_id=project_id)
        
    task_id=request.GET.get('task_id')
    if(task_id is not None):
        tasks=Task.objects.filter(code=task_id)
        
    tasks_data=[]
    for task in tasks:
        task_data={}
        task_data['id']=task.id
        task_data['assignee']=task.assignee.username
        task_data['assignee_id']=task.assignee.id
        task_data['creator']=task.creator.username
        task_data['reportor']=task.reportor.username
        task_data['title']=task.title
        task_data['description']=task.description
        task_data['notes']=task.notes
        task_data['state']=task.state
        task_data['priority']=task.priority
        task_data['start_date']=task.start_date
        task_data['due_date']=task.due_date
        task_data['create_at']=task.create_at
        task_data['code']=task.code
        task_data['project_id']=task.project.id
        task_data['project_code']=task.project.code
        task_data['project_name']=task.project.name
        tasks_data.append(task_data)
        
    return Response(tasks_data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_projects(request):
   
    projects=Project.objects.all()

    user_id=request.GET.get('user_id')
    if(user_id is not None):
        projects = Project.objects.filter(peopleinproject__user=user_id).distinct()
    # for i in range(10):
    projects_data=[]
    for project in projects:
        teamsize = PeopleInProject.objects.filter(project=project).count()
        task = Task.objects.filter(project=project)
        open_task=task.filter(state=1).count()
        in_progress_task=task.filter(state=2).count()
        done_task=task.filter(state=3).count()
        on_hold_task=task.filter(state=4).count()
        project_data={}
        project_data['id']=project.id
        project_data['name']=project.name
        project_data['description']=project.description
        project_data['state']=project.state
        project_data['code']=project.code
        project_data['start_date']=project.start_date
        project_data['due_date']=project.due_date
        project_data['create_at']=project.create_at
        project_data['pic']=project.pic.username
        project_data['open_task']=open_task
        project_data['in_progress_task']=in_progress_task
        project_data['done_task']=done_task
        project_data['on_hold_task']=on_hold_task
        project_data['total_task']=task.count()
        project_data['teamsize']=teamsize
        projects_data.append(project_data)
        
    return Response(projects_data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comments(request):
    task = Task.objects.get(code=request.GET.get("task_code"))
    comments=Comment.objects.filter(task=task).order_by('-create_at')
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
    proejct.code= body['code']
    proejct.pic= UserAccount.objects.get(id=body['leader'])
    proejct.create_at= datetime.now()

    proejct.save()

    peopleIn=PeopleInProject()
    peopleIn.project=proejct
    peopleIn.user=UserAccount.objects.filter(id=request.user.id).first()
    peopleIn.save()
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    body = json.loads(request.body)
    task=Task()
    project = Project.objects.get(id=body['project_id'])
    task.project = project
    task.creator=UserAccount.objects.get(id=request.user.id)
    task.assignee=UserAccount.objects.get(id=body['assignee']) #assignee id
    task.reportor=UserAccount.objects.get(id=body['reportor']) #assignee id

    task.title = body['name']
    task.description=body['description']
    # task.notes= body['notes']
    task.state=body['state']
    task.priority= body['priority']
    task.start_date= body['start_date']
    task.due_date= body['due_date']
    task.create_at= datetime.now()
    task.last_update= datetime.now()
    task.save()

    formatted_number = "{0:0=3d}".format(task.id)
    # print("formatted_number ID===")
    task.code = project.code+"-" + formatted_number
    task.save()

    create_event(task.creator,"create",task,None)

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
# def create_event(user,action,task,message):

    create_event(comment.creator,"comment",comment.task,comment.message)
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def modify_task(request):
    body = json.loads(request.body)
    task=Task.objects.get(id=body['task_id'])

    if 'assignee' in body:
        task.assignee=UserAccount.objects.get(id=body['assignee']) #assignee id
    if 'reportor' in body:
        task.reportor=UserAccount.objects.get(id=body['reportor']) #assignee id
    if 'name' in body:
        task.name = body['name']
    if 'notes' in body:
        task.notes = body['notes']
    if 'description' in body:
        task.description=body['description']
    if 'state' in body:
        task.state=body['state']
    if 'priority' in body:
        task.priority=body['priority']
    if 'start_date' in body:
        task.start_date= body['start_date']
    if 'due_date' in body:
        task.due_date= body['due_date']
    if 'project_id' in body:
        task.project = Project.objects.get(id=body['project_id'])

    create_event(request.user,"change state of",task,None)

    task.save()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_people_in_projct(request):
    body = json.loads(request.body)
    people_project = PeopleInProject()
    people_project.project=Project.objects.filter(code=body['project_id']).first()
    people_project.user=UserAccount.objects.get(id=body['user_id'])
    people_project.save()

    return Response(status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_people_in_projct(request):
    body = json.loads(request.body)
    print(body['project_id'])
    print(body['user_id'])
    print("HELLOooooooooooooo")
    project = Project.objects.filter(code=body['project_id']).first()
    user = UserAccount.objects.get(id=body['user_id'])
    PeopleInProject.objects.filter(Q(project=project)&Q(user=user)).delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_event(request):
    user_id=request.user.id
    projects = Project.objects.filter(peopleinproject__user=user_id).distinct()
    tasks=Task.objects.filter(project__in =projects)
    events = Event.objects.filter(task__in=tasks)

    events_data=[]
    for event in events:
        evenet_data={}
        evenet_data["user"]=event.user.username
        evenet_data["userId"]=event.user.id
        evenet_data["action"]=event.action
        evenet_data["taskId"]=event.task.code
        evenet_data["name"]=event.task.title
        evenet_data["message"]=event.message
        evenet_data["create_at"]=event.create_at
        events_data.append(evenet_data)

    return Response(events_data)


def create_event(user,action,task,message):
    event=Event()
    event.user=user
    event.action=action
    event.task=task
    event.message=message
    event.create_at=datetime.now()
    event.save()
    return


