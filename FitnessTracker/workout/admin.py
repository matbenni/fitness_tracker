from django.contrib import admin
from .models import WorkoutSession, WorkoutSets, Exercises

# Register your models here.
admin.site.register([WorkoutSession, WorkoutSets, Exercises])