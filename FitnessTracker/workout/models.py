from django.db import models
from django.conf import settings
from datetime import timedelta

# Create your models here.
# If you don't define a primary key field in your model, Django automatically adds a field named id
class Equipment(models.Model):
    equipment_name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="admin")
    date_added = models.DateField(auto_now_add=True)
    last_updated_date = models.DateField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.equipment_name

class MuscleGroups(models.Model):
    muscle_group_name = models.CharField(max_length=20, null=False, blank=False, unique=True)

    def __str__(self):
        return self.muscle_group_name

class Exercises(models.Model):
    class Units(models.TextChoices):
        lbs = "lbs"
        kg = "kg"
        bw = "bodyweight"
        time = "time"
        distance = "distance"

    class Type(models.TextChoices):
        weight_and_reps = "Weight and Reps"
        distance_and_time = "Distance and Time"
        # Premium Types
        weight_and_distance = "Weight and Distance"
        weight_and_time = "Weight and Time"
        reps_and_distance = "Reps and Distance"
        reps_and_time = "Reps and Time"
        weight = "Weight"
        reps = "Reps"
        distance = "Distance"
        time = "Time"

    name = models.CharField(max_length=95, unique=True)
    description = models.TextField(null=True, blank=True)
    default_unit = models.CharField(choices=Units, default=Units.lbs)
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="admin")
    muscle_group = models.ManyToManyField(MuscleGroups)
    exercise_type = models.CharField(choices=Type, default=Type.weight_and_reps)

    def __str__(self):
        return self.name

class WorkoutSession(models.Model):
    # A workout contains one or more sets
    create_date = models.DateField(auto_now_add=True)
    last_updated_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=25, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

class WorkoutSets(models.Model):
    # A set contains one or more exercises
    workout_session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE)
    is_supserset = models.BinaryField(null=True, blank=True)
    exercise_value = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    weight_lb = models.DecimalField(decimal_places=2, max_digits=5, default=0, null=True, blank=True)
    weight_kg = models.DecimalField(decimal_places=2, max_digits=5, default=0, null=True, blank=True)
    reps = models.IntegerField(default=0, null=True, blank=True)
    distance_mi = models.DecimalField(decimal_places=2, max_digits=5, default=0, null=True, blank=True)
    distance_km = models.DecimalField(decimal_places=2, max_digits=5, default=0, null=True, blank=True)
    time_minutes = models.DecimalField(decimal_places=2, max_digits=5, default=0, null=True, blank=True)
    time_seconds = models.DecimalField(decimal_places=2, max_digits=5, default=0, null=True, blank=True)   