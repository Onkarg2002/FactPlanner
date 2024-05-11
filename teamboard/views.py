import json 
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from teamboard.models import Boardmodel, TaskModel
from teamboard.serializer import ProjectSerrializer, TaskSerializer

class TeamBoardBase(APIView):
    
    db_folder = r"C:\Users\user\OneDrive\Desktop\FactPlanner\Project_Planner_tool\db"
    file_name = "teamboard_data.json"
    
    """
    Base interface implementation for APIs to manage team boards.
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
        if 'user_id' in request.data:
            id = self.add_task(request)
            return Response({"id":id}, status=status.HTTP_201_CREATED)
        elif len(request.data) == 3 :
            id = self.create_board(request)
            return Response({"id":id}, status=status.HTTP_201_CREATED)
        elif len(request.data) == 2 :
            id = self.update_task_status(request.data['id'],request.data['status'])
            return Response("Updated Successfully")
        elif len(request.data) == 1:
            boards = self.list_boards(request.data['id'])
            return Response(boards)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        if 'id' in request.data:
            boards = self.list_boards(request.data['id'])
            return Response(boards)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None, format=None):
        if pk is not None:
            self.update_board(request, pk)
            return Response("Updated Successfully")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        if pk is not None:
            self.update_board(request, pk)
            return Response("Updated Successfully")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def create_board(self, request, format=None):
        serializer = ProjectSerrializer(data=request.data)
        if serializer.is_valid():
            data = self.read_data_from_file()
            board_id = str(len(data) + 1) 
            serializer.save(id=board_id)  # Assuming ID is not part of request data
            data[board_id] = serializer.data  # Add data to the dictionary
            self.write_data_to_file(data)  # Write data back to the file
            return Response({"id": board_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def close_board(self, pk):
        data = self.read_data_from_file()
        teamid = Boardmodel.objects.filter(id=pk).values('team')
        statuses = TaskModel.objects.filter(user_id__in=teamid).values_list('status', flat=True)
        if all(status == 'closed' for status in statuses):
            Boardmodel.objects.filter(id=pk).update(status='closed')
            self.write_data_to_file(data)

    def add_task(self, request):
        statusss = Boardmodel.objects.filter(team=request.data['user_id']).values('status')
        if all(status['status'] == 'open' for status in statusss):
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return serializer.data.get('id')

    def update_task_status(self, pk, status):
        TaskModel.objects.filter(id=pk).update(status=status)

    def list_boards(self, pk):
        query = Boardmodel.objects.filter(team=pk).values('id','name').all()
        return query

    def export_board(self, request: str) -> str:
        pass

    def update_board(self, request, pk):
        data = self.read_data_from_file()
        serializer = ProjectSerrializer(data=request.data)
        if serializer.is_valid():
            serializer.save(id=pk)
            data[pk] = serializer.data
            self.write_data_to_file(data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
