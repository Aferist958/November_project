# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from .serializers import CreateProjectSerializer
#
#
# # Create your views here.
# @api_view(['POST'])
# def create_project(request):
#     serializer = CreateProjectSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     project = serializer.save()
#     return Response({'project': project}, status=status.HTTP_200_OK)
