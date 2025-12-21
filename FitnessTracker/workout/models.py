from django.db import models
from django.conf import settings

# Create your models here.
# If you don't define a primary key field in your model, Django automatically adds a field named id
class Equipment(models.Model):
    equipment_name = models.CharField(max_length=50, null=False, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    last_updated_date = models.DateField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

class MuscleGroups(models.Model):
    muscle_group_name = models.CharField(max_length=20, null=False, blank=False)

class Exercises(models.Model):
    class Units(models.TextChoices):
        lbs = "lbs"
        kg = "kg"
        bw = "bodyweight"
        time = "time"

    name = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)
    default_unit = models.CharField(choices=Units, default=Units.lbs)
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    muscle_group = models.ForeignKey(MuscleGroups, on_delete=models.CASCADE)

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

    