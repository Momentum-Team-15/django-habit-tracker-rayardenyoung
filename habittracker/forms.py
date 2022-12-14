from django import forms
from .models import Habit, DailyRecord

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ['name', 'target', 'unit_of_measure', 'user']

class DailyRecordForm(forms.ModelForm):

    class Meta:
        model = DailyRecord
        fields = ['amount', 'completed_date']


class EditDailyRecordForm(forms.ModelForm):

    class Meta:
        model = DailyRecord
        fields = ('amount', 'completed_date')
