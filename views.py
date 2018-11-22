from django.shortcuts import render, redirect
from .form import AddTaskForm, Task, ReportForm
from django.contrib.auth.models import User,Group

# Create your views here.


def add_task(request):
    form = AddTaskForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        form = AddTaskForm()
    else:
        form = AddTaskForm()
    return render(request, 'AddTaskForm.html', {'form': form})


def Reports(request):
    form = ReportForm(request.POST)
    if request.method == 'POST':
        form.save()
        form = ReportForm()
    else:
        form = ReportForm()
    return  render(request, 'Reports.html', {'form':form})



def showTaskExecutor(request):
    username = None
    if request.user.is_authenticated:
            username = request.user.username
    if request.user.is_authenticated:
        Tasks = Task.objects.filter(TaskExecutor = request.user)
    elif username == 'admin':
        Tasks = Task.objects.all()
    return render(request, 'TaskList.html', {'Tasks': Tasks})
