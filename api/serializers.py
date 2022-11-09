from rest_framework import serializers
from habittracker.models import Habit



class HabitSerializer(serializers.ModelSerializer):
    #specifying how the json should look:
    class Meta:
        model = Habit
        fields = ['id', 'name', 'target', 'unit_of_measure', 'user']