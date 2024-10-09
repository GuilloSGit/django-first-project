from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('hoteles', views.hoteles, name='hoteles'),
    path('comidas', views.comidas, name='comidas'),
    path('comercios', views.comercios, name='comercios'),
    path('hospitales', views.hospitales, name='hospitales'),
    path('transporte', views.transporte, name='transporte'),
    path('bancos', views.bancos, name='bancos'),
    path('emergencias', views.emergencias, name='emergencias'),
    path('farmacias', views.farmacias, name='farmacias'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasksByProjNum/<int:number>', views.tasksByProjNum, name='tasksByProjNum'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project'),
    path('mark-as-done/<int:task_id>/', views.mark_as_done, name='mark-as-done'),
    path('soft-delete/<int:task_id>/', views.soft_delete, name='soft-delete')
]