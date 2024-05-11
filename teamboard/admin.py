from django.contrib import admin
from teamboard.models import TaskModel, Boardmodel


@admin.register(Boardmodel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'Project_name', 'Project_Description', 'created_at', 'team', 'status']

@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'Project_title', 'Project_description', 'team', 'created_at', 'status']
