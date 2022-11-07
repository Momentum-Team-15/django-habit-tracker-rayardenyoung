from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit, DailyRecord
from habittracker.forms import HabitForm, DailyRecordForm, EditDailyRecordForm

# Create your views here.

@login_required
def index(request):
    habits = Habit.objects.all()
    return render(request, 'habittracker/index.html', {'habits': habits})

def logout(request):
    return render(request, 'accounts/logout/')

def login(request):
    return render(request, 'accounts/login/')

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    return render(request, 'habittracker/habit_detail.html', {'habit': habit})

def create_habit(request):
    if request.method == 'POST':
        #if user is submitting the form
        form = HabitForm(request.POST, request.FILES)
        #form is the filled out ("bound") form with user data
        if form.is_valid():
            #django checks if form is valid (filled out with no missing or mistyped data)
            habit = form.save()
            #because it's a ModelForm, saving it will create an instance of Habit in the database
            #only need commit=False if you are going to add additional data not on the form (like request.user)
            return redirect("home")
    else: 
        form = HabitForm()
        #^^^if user is visiting a page with GET request, not submitting the form yet, render a blank
    return render(request, 'habittracker/create_habit.html', {'form': form})

def edit_habit(request, habitpk):
    habit = get_object_or_404(Habit, pk=habitpk)
    if request.method == "POST":
        form = HabitForm(request.POST, request.FILES, instance=habit)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('habit_detail', pk=habit.pk)
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habittracker/edit_habit.html', {'form': form})

def delete_habit(request, habitpk):
    habit = get_object_or_404(Habit, pk=habitpk)
    if request.method == "POST":
        habit.delete()
        return redirect('home')
    return render(request, 'habittracker/delete_habit.html')

def create_dailyrecord(request):
    if request.method == 'POST':
        form = DailyRecordForm(request.POST, request.FILES)
        if form.is_valid():
            dailyrecord = form.save()
            return redirect("home")
    else: 
        form = DailyRecordForm()
    return render(request, 'habittracker/create_dailyrecord.html', {'form': form})

def edit_dailyrecord(request, habitpk, dailyrecordpk):
    dailyrecord = DailyRecord.objects.get(pk=habitpk)
    if request.method == "POST":
        form = EditDailyRecordForm(request.POST, request.FILES, instance=dailyrecord)
        if form.is_valid():
            dailyrecord = form.save(commit=True)
            dailyrecord.save()
            return redirect('home')
    else:
        form = EditDailyRecordForm(instance=dailyrecord)
    return render(request, 'habittracker/edit_dailyrecord.html', {'form': form})