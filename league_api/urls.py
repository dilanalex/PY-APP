from django.urls import path, include
from .views import (
    ApiTestListApiView,
)

urlpatterns = [
    path('api', ApiTestListApiView.as_view()),
]