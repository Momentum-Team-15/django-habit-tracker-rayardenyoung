from django.shortcuts import render
from .models import Habit

# Create your views here.

def index(request):
    return render(request, 'habittracker/index.html')
