from django.db import models
from teams.models import team


class Boardmodel(models.Model):
    choice = (
        ('Complete','Complete'),
        ('Active','Active'),
        ('Pending','Pending'),
    )
    Project_name = models.CharField(max_length=64, unique=True)
    Project_Description = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey(team,help_text='Select team for this project', on_delete=models.CASCADE)
    status = models.CharField(max_length=15 ,choices=choice, default='OPEN')

    def __str__(self) -> str:
        return self.Project_name

class TaskModel(models.Model):
    choice = (
        ('Complete','Complete'),
        ('Active','Active'),
        ('Pending','Pending'),
    )
    Project_title = models.CharField(max_length=64, unique=True)
    Project_description = models.CharField(max_length=128)
    team = models.ForeignKey(team, help_text="Select the team for the task", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15 ,choices=choice, default='OPEN')

    def __str__(self) -> str:
        return self.Project_title