# Fact Planner

The Project Planning Tool is a comprehensive solution for managing projects, consisting of APIs developed in Django Rest Framework.

## Installation

1. Install the required dependencies listed in `requirements.txt` by executing the command `pip install -r requirements.txt` in the root folder.
2. Install Postman for testing APIs.

Before running the application, execute the following commands in the root folder:


python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## Description

The Project Planning Tool is a Django project named `Fact Planner`, comprising three distinct apps:

1. **User**: Manages user-related functionalities.
2. **Team**: Handles team-related operations.
3. **ProjectBoard**: Facilitates project board management.

## API Reference

### User's APIs

- **GET all users**: `http://localhost:8000/users/`
- **GET user by ID**: `http://localhost:8000/users/<int:pk>/`

### Team's APIs

- **GET all teams**: `http://localhost:8000/teams/`
- **GET team by ID**: `http://localhost:8000/teams/<int:pk>/`

### Project Board's APIs

- **GET all project boards**: `http://localhost:8000/teamboard/`
- **GET project board by ID**: `http://localhost:8000/teamboard/<int:pk>/`

### Conclusion
The Project Planning Tool offers a robust platform for efficiently managing projects through its Django-based architecture and RESTful APIs. With seamless installation steps and clear API references, it provides a user-friendly experience for developers and project managers alike.

By encompassing three distinct apps—User, Team, and ProjectBoard—the tool caters to various project management needs, from user management to team collaboration and project board organization. Users can easily interact with the APIs to retrieve information about users, teams, and project boards, enhancing the transparency and accessibility of project data.

With its flexibility, scalability, and ease of use, the Project Planning Tool stands as an invaluable asset for teams and organizations seeking a streamlined approach to project planning and execution. Whether used as a standalone solution or integrated into existing workflows, this tool empowers teams to efficiently navigate the complexities of project management, ultimately driving productivity and success.
