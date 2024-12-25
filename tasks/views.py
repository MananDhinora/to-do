from django.shortcuts import render, redirect
from .models import Task


def home(request):
    return render(request, "index.html", {"tasks": Task.objects.all()})

def remaining_task(request):
    return render(request, "remaining.html", {"tasks": Task.objects.filter(completed=False)})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        due_time = request.POST.get("due_time")

        if title != "" and due_date != "" and due_time != "":
            task = Task(
                    title=title,
                    description=description,
                    due_date=due_date,
                    due_time=due_time)
            task.save()
            return redirect("remaining")
    return render(request, "add_task.html")

def completed_task(request):
    return render(request, "completed.html",{"tasks": Task.objects.filter(completed=True)})

def delete_task(request, task_id):
    return render(request, "delete.html", {"task": Task.objects.get(id=task_id)})

def task_detail(request, task_id):
    return render(request, "task_detail.html", {"task": Task.objects.get(id=task_id)})

def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect(request.META.get("HTTP_REFERER"))

def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect(request.META.get("HTTP_REFERER"))

