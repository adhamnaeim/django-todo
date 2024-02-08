from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

     
    context = {
        'tasks' : tasks,
        'form' : form
    }
    return render(request, 'tasks/index.html', context)


def update_task(request,id):
    task = Task.objects.get(id=id)
    
    form = TaskForm(instance=task)
    context = {
        'form': form,  
    }
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'tasks/update_task.html',context)