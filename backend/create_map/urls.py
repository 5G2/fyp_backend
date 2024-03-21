from django.urls import path
from . import views

urlpatterns=[
    path('getTasks/',views.get_tasks),
    path('getTaskCountByGroup/',views.get_task_count_by_group),
    path('getSevenDaysTasksNumber/',views.get_7days_task),
    path('getTotalTaskNumber/',views.get_total_task_number),
    path('getProjects/',views.get_projects),
    path('getAllUser/',views.get_all_user),
    path('getUserData/',views.get_user_data),
    path('getComments/',views.get_comments),
    path('getEvent/',views.get_event),
    path('createProject/',views.create_project),
    path('createTask/',views.create_task),
    path('createComment/',views.create_comment),
    path('modifyTask/',views.modify_task),
    path('addPeopleInProject/',views.add_people_in_projct),
    path('deletePeopleInProject/',views.delete_people_in_projct),
]
