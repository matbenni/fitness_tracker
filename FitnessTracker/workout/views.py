from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def profile(request):
    return render(request, "profile.html")

def new_workout(request):
    return render(request, "new_workout.html")

def my_workouts(request):
    return render(request, "my_workouts.html")

def my_exercises(request):
    return render(request, "my_exercises.html")