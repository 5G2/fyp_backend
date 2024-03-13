from django.urls import path
from . import views

urlpatterns=[
    path('getTasks/',views.get_tasks),
    path('getProjects/',views.get_projects),
    path('getComments/',views.get_comments),
    path('createProject/',views.create_project),
    path('createTask/',views.create_task),
    path('createComment/',views.create_comment),
]
