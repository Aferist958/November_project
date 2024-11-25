# from django.db import models
# from django.db.models import TextField, CharField
#
# from api.users.models import CustomUser
#
#
# # Create your models here.
#
# class Project_User(CustomUser):
#     role_choice = {
#         'BACKEND': 'Бэкенд разработчик',
#         'FRONTEND': 'Фронтенд разработчик',
#         'PROJECT_MANAGER': 'Проджект мэнеджер',
#         'ANALYST': 'Аналитик',
#         'DESIGNER': 'Дизайнер',
#         'CONCEPTOLOGIST': 'Концептолог'
#     }
#     role = models.CharField(max_length=30, choices=role_choice, default=None)
#
#
# # Create your models here.
# class Project(models.Model):
#     status_choice = {
#         'ACTIVE': 'Активен',
#         'ARCHIVED': 'Архивирован'
#     }
#     name = CharField(max_length=100)
#     desk = TextField()
#     date_create = models.DateTimeField(auto_now_add=True)
#     date_update = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=25, choices=status_choice)
#     users = models.ManyToManyField(Project_User, blank=True)
