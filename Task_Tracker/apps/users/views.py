from django.shortcuts import render
from .models import User
from .serializers import UserSignupSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

@api_view(['POST'])
def signup(request):
    data = request.data
    serializer = UserSignupSerializer(data=data)
    if serializer.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(email=data['email'], name=data['name'], surname=data['surname'], role=data['role'], password=make_password(data['password']))
            user.save()
            user = User.objects.create()
            return Response({'message':'User Created Successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'User Already Exists'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def login(request):
    data = request.data
    if User.objects.filter(username=data['email']).exists():
        user = User.objects.get(username=data['email'])
        if user.check_password(data['password']):
            return Response(UserSerializer(instance=user).data, status=status.HTTP_200_OK)
        else:
            return Response({'message':'Invalid Password'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
