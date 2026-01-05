from django.urls import path, include
from . import views

app_name = "workout_url_app"

urlpatterns = [
    path('', views.new_workout, name="workout"),
    path('my-workouts/', views.my_workouts, name="my_workouts"),
    path('new-workout/', views.new_workout, name="new_workout"),
    path('my-exercises/', views.my_exercises, name="my_exercises"),
    path('new-exercise/', views.new_exercise, name="new_exercise"),
    # path('about/', views.about, name="about"),
]