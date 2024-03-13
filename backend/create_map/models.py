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
    start_date = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True)
    create_at = models.DateTimeField(null=True)

class Task(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    assignee=models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True,related_name='assignee')
    creator=models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True,related_name='creator')
    reportor=models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True,related_name='reportor')
    name=models.TextField(max_length=20,null=True)
    description=models.TextField(max_length=20,null=True)
    notes=models.TextField(max_length=20,null=True)
    state = models.IntegerField(null=True, default=0)
    priority=models.IntegerField(null=True, default=0)
    start_date = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True)
    create_at = models.DateTimeField(null=True)

class Comment(models.Model):
    task=models.ForeignKey(Task, on_delete=models.CASCADE,null=True)
    creator=models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True)
    message=models.TextField(max_length=500,null=True)
    create_at = models.DateTimeField(null=True)

class event(models.Model):
    user=models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True)
    task=models.ForeignKey(Task, on_delete=models.CASCADE,null=True)
    action=models.TextField(max_length=500,null=True)
    message=models.TextField(max_length=500,null=True)
