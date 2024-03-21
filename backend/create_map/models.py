from django.db import models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from accounts.models import UserAccount
# Create your models here.
#Delete null=True in some field, check if need delete

class Project(models.Model):
    name=models.TextField(max_length=20,null=True)
    description=models.TextField(max_length=20,null=True)
    state = models.IntegerField(null=True, default=0)
    start_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    create_at = models.DateField(null=True)
    code = models.TextField(max_length=3,null=True)
    pic = models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True)

class Task(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    assignee=models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True,related_name='assignee')
    creator=models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True,related_name='creator')
    reportor=models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True,related_name='reportor')
    title=models.TextField(max_length=20,null=True)
    description=models.TextField(max_length=20,null=True)
    notes=models.TextField(max_length=20,null=True)
    #state 1=open 2=in-progress 3=done 4=on-hole
    state = models.IntegerField(null=True, default=0)
    priority=models.IntegerField(null=True, default=0)
    start_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    create_at = models.DateField(null=True)
    last_update = models.DateTimeField(null=True)
    code= models.TextField(max_length=30,null=True)
    

class Comment(models.Model):
    task=models.ForeignKey(Task, on_delete=models.CASCADE,null=True)
    creator=models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True)
    message=models.TextField(max_length=500,null=True)
    create_at = models.DateTimeField(null=True)

class Event(models.Model):
    user=models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True)
    task=models.ForeignKey(Task, on_delete=models.CASCADE,null=True)
    action=models.TextField(max_length=500,null=True)
    message=models.TextField(max_length=500,null=True)
    create_at=models.DateTimeField(null=True)


class PeopleInProject(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True)
