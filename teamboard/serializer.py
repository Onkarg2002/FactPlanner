from teamboard.models import TaskModel, Boardmodel
from rest_framework import serializers

class ProjectSerrializer(serializers.ModelSerializer):
    class Meta:
        model = Boardmodel
        fields = ['id', 'Project_name', 'Project_Description', 'created_at', 'team', 'status']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id', 'Project_title', 'Project_description', 'team', 'created_at', 'status']
