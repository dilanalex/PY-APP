from django.urls import path, include
from .views import (
    ApiTestListApiView,
    ScoreBoardAPIView,
    TeamAPIView,
)

urlpatterns = [
    path('api_test', ApiTestListApiView.as_view()),
    path('scoreboard', ScoreBoardAPIView.as_view()),
    path('team/', TeamAPIView.as_view()),
    path('team/<int:team_id>/', TeamAPIView.as_view()),
]