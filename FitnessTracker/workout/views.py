from django.shortcuts import render, redirect
from workout.models import Exercises, MuscleGroups, Equipment
from FitnessTracker.forms import ExerciseForm
from users.models import UserProfile
from django.contrib.auth.models import User
from django.db.models.functions import Lower

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

    context = {}
    
    muscle_groups = MuscleGroups.objects.all()
    admin_user = User.objects.filter(username="admin").values_list('username', flat=True)
    current_user = request.user.username
    exercise_list = Exercises.objects.filter(author__username__in=[admin_user, current_user]).order_by(Lower("name"))

    context['muscle_groups'] = muscle_groups
    context['exercise_list'] = exercise_list

    return render(request, "my_exercises.html", context)

def new_exercise(request):

    context = {}

    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            new_exercise = form.save(commit=False)
            new_exercise.author = request.user
            new_exercise.save()
            return redirect("workout_url_app:my_exercises")
    else:
        form = ExerciseForm()

    context['form'] = form

    return render(request, "new_exercise.html", context)
    