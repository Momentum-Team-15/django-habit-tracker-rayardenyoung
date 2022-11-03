from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Habit(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name

class Record(models.Model):
    pass


class User(AbstractUser):
    pass