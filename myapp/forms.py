from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Título de la tarea", max_length=100, widget=forms.TextInput(attrs={ 'class': 'input'}))
    description = forms.CharField(label="Descripción de la tarea", required=False, widget=forms.TextInput(attrs={ 'class': 'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=75, widget=forms.TextInput(attrs={'class': 'input'}))