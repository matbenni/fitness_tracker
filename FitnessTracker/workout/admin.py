from django.contrib import admin
from .models import WorkoutSession, WorkoutSets, Exercises, MuscleGroups, Equipment

# Register your models here.
admin.site.register([WorkoutSession, WorkoutSets, Exercises, MuscleGroups, Equipment])