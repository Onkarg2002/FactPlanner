from teams.models import team
from rest_framework import serializers

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = team
        fields = ['id', 'Team_Name', 'Team_description', 'created_at', 'admin', 'members']

class TeamGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = team
        fields = ['Team_Name', 'Team_description', 'created_at', 'admin']

class TeamPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = team
        fields = ['id', 'Team_Name', 'Team_description', 'created_at', 'admin']