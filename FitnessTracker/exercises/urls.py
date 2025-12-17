from django.urls import path
from . import views

app_name = "exercises_url_app"

urlpatterns = [
    path('', views.user_exercises_list, name="user_exercises_list"),
    # path('about/', views.about, name="about"),
]