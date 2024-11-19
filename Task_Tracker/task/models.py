from django.db import models
from django.db.models import ForeignKey

# from project.models import Project
# from users.models import Profile


# Create your models here.
class Task(models.Model):
    priority = {
        'LOW': 'Низкий',
        'MEDIUM': 'Средний',
        'HIGH': 'Высокий'
    }
    name = models.CharField(max_length=100)
    desc = models.TextField()
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # executor = models.ForeignKey(Profile, on_delete=models.CASCADE)
