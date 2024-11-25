from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .serializers import  RegSerializer


@api_view(['POST'])
def log_in_user(request):
    data = request.data
    email = data.get('email', None)
    password = data.get('password', None)
    if email is None or password is None:
        return Response({'error': 'Нужен и email, и пароль'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(email=email, password=password)
    if user is None:
        return Response({'error': 'Неверные данные'},

                        status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    refresh.payload.update({
        'user_id': user.id,
        'email': user.email
    })
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
def sign_up_user(request):
    serializer = RegSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    refresh.payload.update({  # Полезная информация в самом токене
        'user_id': user.id,
        'email': user.email
    })
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),  # Отправка на клиент
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def log_out_user(request):
    refresh_token = request.data.get('refresh_token')  # С клиента нужно отправить refresh token
    if not refresh_token:
        return Response({'error': 'Необходим Refresh token'},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        token = RefreshToken(refresh_token)
        token.blacklist()  # Добавить его в чёрный список
    except Exception as e:
        return Response({'error': 'Неверный Refresh token'},
                        status=status.HTTP_400_BAD_REQUEST)
    return Response({'success': 'Выход успешен'}, status=status.HTTP_200_OK)

