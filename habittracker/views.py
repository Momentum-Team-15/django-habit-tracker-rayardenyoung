from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Habit

# Create your views here.

@login_required
def index(request):
    return render(request, 'habittracker/index.html')

# def login(request):
#     return render(request, 'accounts/login/')


def logout(request):
    return render(request, 'accounts/logout/')
