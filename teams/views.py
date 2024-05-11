import json 
import os
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from teams.models import team, user
from teams.serializers import TeamSerializer, TeamGETSerializer, TeamPOSTSerializer

class TeamBase(APIView):
    
    db_folder = r"C:\Users\user\OneDrive\Desktop\FactPlanner\Project_Planner_tool\db"
    file_name = "teams_data.json"

    """
    Base interface implementation for APIs to manage teams.
    For simplicity, a single team manages a single project, and there is a separate team per project.
    Users can be...
    """ 

    def get_data_file(self):
        return os.path.join(self.db_folder, self.file_name)

    def read_data_from_file(self):
        data_file = self.get_data_file()
        if not os.path.exists(data_file):
            return {}
        with open(data_file, "r") as f:
            return json.load(f)

    def write_data_to_file(self, data):
        data_file = self.get_data_file()
        with open(data_file, "w") as f:
            json.dump(data, f, indent=4)


    def post(self, request, format=None):
        response = self.create_team(request)
        return response

    def get(self, request, pk=None, format=None):
        if 'id' in request.data:
            response = self.list_team_users(request.data['id'])
        elif pk is None:
            response = self.list_teams()
        elif pk is not None:
            response = self.describe_team(pk)
        return response

    def patch(self, request, pk=None, format=None):
        response = self.update_team(request, pk)
        return response

    def put(self, request, pk=None, format=None):
        response = self.add_users_to_team(request, pk)
        return response
        
    # create a team
    def create_team(self, request):
        """
        Create a new team.

        :param request: A json string with the team details
        :return: A json string with the response {"id" : "<team_id>"}

        Constraints:
            * Team name must be unique
            * Name can be max 64 characters
            * Description can be max 128 characters
        """
        serializer = TeamPOSTSerializer(data=request.data)
        if serializer.is_valid():
            data = self.read_data_from_file()
            team_id = str(len(data) + 1) 
            serializer.save(id=team_id) 
            data[team_id] = serializer.data 
            self.write_data_to_file(data)
            serializer.save()
            return Response({"id":serializer.data.get('id')}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def list_teams(self):
        """
        List all teams or describe a specific team.

        :return: A json list with the response if no specific team is mentioned.
                 A json string with the response if a specific team is described.
        """
        teams = team.objects.all()
        serializer = TeamGETSerializer(teams, many=True)
        return Response(serializer.data)

    
    def describe_team(self, pk) -> str:
        """
        Describe a specific team.

        :param pk: The primary key of the team.
        :return: A json string with the response.
        """
        team_instance = team.objects.get(id=pk)
        serializer = TeamGETSerializer(team_instance)
        return Response(serializer.data)

    
    def update_team(self, request, pk=None, format=None):
        """
        Update a team.

        :param request: A json string with the team details.
        :param pk: The primary key of the team.
        :return: A json string with the response.
        """

        team_instance = team.objects.get(id=pk)
        serializer = TeamSerializer(team_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"MSG": "Team Updated Successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def add_users_to_team(self, request, pk):
        """
        Add users to a team.

        :param request: A json string with the team details.
        :param pk: The primary key of the team.
        :return: A json string with the response.
        """
        id = pk
        existing_users = team.objects.filter(id=pk).values_list('members')
        print(existing_users)
        return Response({"MSG": "Team Updated Successfully"})

    
    def remove_users_from_team(self, request: str):
        """
        Remove users from a team.

        :param request: A json string with the team details.
        :return: A json string with the response.
        """
        pass

   
    def list_team_users(self, id):
        """
        List all users of a team.

        :param id: The primary key of the team.
        :return: A json list with the response.
        """
        user_list = team.objects.filter(id=id).values("members")
        user_data = []
        for user_id in user_list:
            users = user.objects.filter(id=user_id["members"]).values("id", "username", "name")
            for user_data_item in users:
                user_data.append(user_data_item)
        return Response(user_data)
