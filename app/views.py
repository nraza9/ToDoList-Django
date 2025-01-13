from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
# File: views.py

# View for displaying tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
    # return HttpResponse('Hello World !')

# View for adding a task
def add_task(request):
    print('========= add_task')
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return redirect('app:task_list')
    return render(request, 'add_task.html')

# View for deleting a task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('app:task_list')
    # return HttpResponse('delete_task')