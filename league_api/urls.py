from django.urls import path, include
from .views import (
    ApiTestListApiView,
    ScoreBoardAPIView,
)

urlpatterns = [
    path('api_test', ApiTestListApiView.as_view()),
    path('scoreboard', ScoreBoardAPIView.as_view()),
]