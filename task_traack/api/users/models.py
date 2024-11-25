from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, TextField


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, name, surname, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, surname=surname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, surname, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, name, surname, password, **extra_fields)

    def create_superuser(self, name, surname, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, name, surname, password, **extra_fields)


# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    # projects = models.ManyToManyField('Project', blank=True)
    # profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")
    USERNAME_FIELD = 'email'
    objects = UserManager()
    REQUIRED_FIELDS = ['name', 'surname',]

    def __str__(self):
        return self.name

