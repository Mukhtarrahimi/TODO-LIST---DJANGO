from django.urls import path
from .views import add_task, task_list, delete_task, edit_task

app_name = "tasks"

urlpatterns = [
    path("", task_list, name="task_list"), 
    path("add/", add_task, name="add_task"),
    path("delete/<int:task_id>",delete_task, name="delete_task" ),
    path("edit/<int:task_id>", edit_task, name="edit_task")
]
