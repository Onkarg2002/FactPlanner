from django.contrib import admin
from teams.models import team
# Register your models here .

@admin.register(team)
class TeamAdmin(admin.ModelAdmin):
    list_display= ['id', 'Team_Name', 'Team_description', 'created_at', 'admin', 'display_members']
