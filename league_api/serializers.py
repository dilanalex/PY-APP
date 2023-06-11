from rest_framework import serializers
from .models import *
class ApiTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiTest
        fields = ["task", "completed", "timestamp", "updated", "user"]
    class Meta:
        model = Game
        fields = ["host", "guest"]
    class Meta:
        model = Team
        fields = ["name"]
    