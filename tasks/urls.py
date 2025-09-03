from django.urls import path
from .views import add_task, task_list

app_name = "tasks"

urlpatterns = [
    path("", task_list, name="task_list"),  # لیست تسک‌ها
    path("add/", add_task, name="add_task"),  # اضافه کردن تسک جدید
]
