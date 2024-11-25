from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser


# class LogSerializer(serializers.Serializer):
#     # Для авторизациии
#     email = serializers.CharField()
#     name = serializers.CharField()
#     surname = serializers.CharField()
#     role = serializers.CharField()
#     password = serializers.CharField()
#
#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')
#         if email and password:
#             user = authenticate(request=self.context.get('request'),
#                                 email=email, password=password)
#         attrs['user'] = user
#         return attrs


class RegSerializer(serializers.ModelSerializer):
    # для регистрации
    password = serializers.CharField(min_length=12)

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'password',]

    def save(self, **kwargs):
        user = CustomUser()
        user.email = self.validated_data['email']
        user.name = self.validated_data['name']
        user.surname = self.validated_data['surname']
        user.set_password(self.validated_data['password'])
        user.save()
        return user


