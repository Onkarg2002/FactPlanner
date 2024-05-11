from django.urls import path
from teamboard.views import TeamBoardBase

urlpatterns = [
    path('teamboard/', TeamBoardBase.as_view(), name='team_board'),
    path('', TeamBoardBase.as_view(), name='get/createteam'),
    path('<int:pk>/', TeamBoardBase.as_view(), name='getspecificteam'),
]
