from django.db import models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your models here.
#Delete null=True in some field, check if need delete

class Project(models.Model):
    name=models.TextField(max_length=20,null=True)
    description=models.TextField(max_length=20,null=True)
    state = models.IntegerField(null=True, default=0)
    rooms=models.TextField(max_length=30,null=True)
    priority=models.IntegerField(null=True, default=0)
    state=models.IntegerField(null=True, default=0)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    create_at = models.DateTimeField(null=True)

class Task(models.Model):
    name=models.TextField(max_length=20,null=True)
    description=models.TextField(max_length=20,null=True)
    state = models.IntegerField(null=True, default=0)
    rooms=models.TextField(max_length=30,null=True)
    priority=models.IntegerField(null=True, default=0)
    state=models.IntegerField(null=True, default=0)
    floor=models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    create_at = models.DateTimeField(null=True)

class User(models.Model):
    first_name=models.TextField(max_length=50,null=True)
    last_name=models.TextField(max_length=50,null=True)
    email=models.TextField(max_length=100,null=True)
    role=models.IntegerField(null=True, default=0)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

class Task(models.Model):
    floor=models.ForeignKey(Task, on_delete=models.CASCADE,null=True)
    floor=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    role=models.IntegerField(null=True, default=0)

class Comment(models.Model):
    floor=models.ForeignKey(Task, on_delete=models.CASCADE,null=True)
    floor=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    message=models.TextField(max_length=500,null=True)
    create_at = models.DateTimeField(null=True)
