from django.http import HttpResponseForbidden
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import *
from .serializers import ApiTestSerializer

## Only for understanding the DJango with Python
##
class ApiTestListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all given requested user
        '''
        testdata = ApiTest.objects.filter(user = request.user.id)
        serializer = ApiTestSerializer(testdata, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create with given  data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = ApiTestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ScoreBoardAPIView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        testdata = Game.objects.all()
        serializer = ApiTestSerializer(testdata, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TeamAPIView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, team_id=None):
        user_role = User_Role.objects.get(user_id=request.user.id)
        if user_role.role.type != 'PLAYER':

            players = Player.objects.filter(team_id=team_id)
            context = {
                'players': players,
                ## Lets pass the average score here #TODO
            }
            serializer = ApiTestSerializer(context, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)