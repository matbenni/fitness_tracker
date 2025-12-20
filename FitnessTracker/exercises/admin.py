from django.contrib import admin
from .models import Exercise
from users.models import UserProfile

# Register your models here.
admin.site.register(Exercise)
admin.site.register(UserProfile)