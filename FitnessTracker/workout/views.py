from django.shortcuts import render
from workout.models import Exercises, MuscleGroups, Equipment
from FitnessTracker.forms import ExerciseForm

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
    exercise_list = Exercises.objects.all().order_by("name")

    context['muscle_groups'] = muscle_groups
    context['exercise_list'] = exercise_list

    return render(request, "my_exercises.html", context)

def new_exercise(request):

    context = {}
    form = ExerciseForm()

    context['form'] = form

    return render(request, "new_exercise.html", context)
    