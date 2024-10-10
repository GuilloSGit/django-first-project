import json
import os
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import Project, Task
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateNewTask, CreateNewProject

# Load data from JSON file
def load_data():
    data_path = os.path.join(settings.BASE_DIR, 'myapp', 'static', 'data', 'data.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def render_data(request, tipo, template):
    data = load_data()
    items = {key: value for key, value in data.get(tipo, {}).items() if key.isdigit()}
    menu_items = menu_navigation(request)
    context = {
        tipo: items,
        'menu_items': menu_items
    }
    return render(request, template, context)

# Navigation items
def menu_navigation(request):
    data = load_data()
    menu_items = {}
    
    # Extrae los elementos del menú del JSON
    for key, value in data.items():
        if 'urlName' in value:
            menu_items[key] = {
                'name': value['urlName'],
                'icon': value['icono'],
                'url': value.get('url', ''),
                'title': value['title']
            }
    
    return menu_items

# Create your views here.
def index(request):
    return render(request, 'index.html', {'menu_items': menu_navigation(request)})

def referentes(request):
    return render(request, 'referentes.html', {'menu_items': menu_navigation(request)})

def hoteles(request):
    return render_data(request, 'hoteles', 'hoteles.html')

def emergencias(request):
    return render_data(request, 'emergencias', 'emergencias.html')

def comercios(request):
    return render_data(request, 'comercios', 'comercios.html')

def hospitales(request):
    return render_data(request, 'hospitales', 'hospitales.html')

def comidas(request):
    return render_data(request, 'comidas', 'comidas.html')

def transporte(request):
    return render_data(request, 'transporte', 'transporte.html')

def bancos(request):
    return render_data(request, 'bancos', 'bancos.html')

def farmacias(request):
    return render_data(request, 'farmacias', 'farmacias.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    tasks = Task.objects.filter(deleted=False)
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def tasksByProjNum(request, number):
    # Obtener el proyecto con el id 'number'
    project = get_object_or_404(Project, id=number)

    # Obtener todas las tareas asociadas al proyecto
    tasks = Task.objects.filter(project=project)

    return render(request, 'tasks/tasksByProjNum.html', {
        'tasks': tasks,
        'project': project
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

@csrf_exempt
def mark_as_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = True
    task.save()
    return JsonResponse({ 'status': 'success' })

@csrf_exempt
def soft_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    print(task)
    task.deleted = True
    task.save()
    return JsonResponse({ 'status': 'success' })
