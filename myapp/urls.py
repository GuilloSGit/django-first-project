from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello, name='welcome'),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasksByProjNum/<int:number>', views.tasksByProjNum, name='tasksByProjNum'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project'),
    path('mark-as-done/<int:task_id>/', views.mark_as_done, name='mark-as-done'),
    path('soft-delete/<int:task_id>/', views.soft_delete, name='soft-delete')
]