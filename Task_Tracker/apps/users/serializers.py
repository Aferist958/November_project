from rest_framework import serializers
from .models import User
from django.contrib.auth.models import User

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'surname', 'role', 'password')

    extra_kwargs = {
        'email': {'required': True, 'allow_blank': False},
        'name': {'required': True, 'allow_blank': False},
        'surname': {'required': True, 'allow_blank': False},
        'role': {'required': True, 'allow_blank': False},
        'password': {'required': True, 'allow_blank': False},
    }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'surname', 'role')
