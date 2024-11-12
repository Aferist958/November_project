from django.db import models
from django.db.models import CharField, TextField


# Create your models here.
class Project(models.Model):
    status_choice = {
        'ACTIVE': 'Активен',
        'ARCHIVED': 'Архивирован'
    }
    name = CharField(max_length=100)
    desk = TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25, choices=status_choice)