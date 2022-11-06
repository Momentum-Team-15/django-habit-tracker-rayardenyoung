from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Habit(models.Model):
    name = models.CharField(max_length=255)
    target = models.PositiveIntegerField(null=True, blank=True)
    unit_of_measure = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits", null=True, blank=True)
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.target} {self.unit_of_measure}"


class DailyRecord(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="records")
    completed_date = models.DateField(blank=True, null=True)
    amount = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Record for {self.habit.name}"

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['habit', 'user', 'completed_date'], name='unique_daily_record')
    # ]

