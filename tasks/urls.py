from django.urls import path
from . import views

urlpatterns=[
        path("", views.home, name=''),
        path("completed", views.completed_task, name='completed'),
        path("remaining", views.remaining_task, name='remaining'),
        path("add_task", views.add_task, name='add_task'),
        path("delete", views.delete_task, name='delete'),
        path("task_detail/<int:task_id>", views.task_detail, name='task_detail'),
        ]
