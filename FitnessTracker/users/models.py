from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Note - setting null=True means that it can be null in the database
# Useing blank=True without null=True means that you set the value to be blank manually
# if the user did not fill out the field. This is just a best practice.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    height_feet = models.IntegerField(max_length=2, null=True, blank=True)
    height_inches = models.IntegerField(max_length=2, null=True, blank=True)
    weight_lbs = models.IntegerField(max_length=3, null=True, blank=True)
    email_verified_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email}'s Profile"