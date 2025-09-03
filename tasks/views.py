from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, "tasks/details.html", {"task": task})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/add_task.html", {"form": form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("tasks:task_list")


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task) 
        if form.is_valid():
            form.save()
            return redirect("tasks:task_list")
    else:
        form = TaskForm(
            instance=task
        )

    return render(request, "tasks/edit_task.html", {"form": form})
