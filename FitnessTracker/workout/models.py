from django.db import models

# Create your models here.
# If you don't define a primary key field in your model, Django automatically adds a field named id
class Exercises(models.Model):
    class Units(models.TextChoices):
        lbs = "lbs"
        kg = "kg"
    name = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)
    default_unit = models.CharField(max_length=3, choices=Units, default=Units.lbs)

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
    # exercise_id = models.ForeignKey()

    