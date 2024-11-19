from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect


# https://developer.mozilla.org/ru/docs/Web/HTTP/Status
# https://www.linkedin.com/pulse/http-status-code-ivan-tay
# https://javaconceptoftheday.com/http-status-codes-cheat-sheet/
# Create your views here.
class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)