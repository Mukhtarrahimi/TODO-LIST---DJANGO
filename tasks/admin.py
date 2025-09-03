from django.contrib import admin
from .models import Task

@admin.register(Task)
class AdminTasks(admin.ModelAdmin):
    list_display = ["title", "content", "created", "completed"]
    list_filter = ["completed", "created"]
    list_editable = ["content", "completed"]
