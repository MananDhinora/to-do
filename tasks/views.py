from django.shortcuts import render, redirect
from .models import Task


def home(request):
    # task = Task.objects.all()
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
            return redirect("/")
    return render(request, "add_task.html")

def completed_task(request):
    return render(request, "completed.html",{"tasks": Task.objects.filter(completed=True)})

def delete_task(request):
    return render(request, "delete.html")

def task_detail(request, task_id):
    return render(request, "task_detail.html", {"tasks": Task.objects.get(task_id)})

