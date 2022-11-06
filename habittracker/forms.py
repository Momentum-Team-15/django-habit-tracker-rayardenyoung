from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ['action', 'target', 'unit_of_measure', 'user']