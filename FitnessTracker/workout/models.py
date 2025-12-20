from django.db import models

# Create your models here.
# If you don't define a primary key field in your model, Django automatically adds a field named id
class WorkoutSession(models.Model):
    create_date = models.DateField(auto_now_add=True)
    last_updated_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=25, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

class WorkoutSets(models.Model):
    workout_session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE)
    