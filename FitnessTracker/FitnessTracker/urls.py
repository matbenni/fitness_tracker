"""
URL configuration for FitnessTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from workout import views as workout_views
from users import views as users_views
from users.views import CustomSignupView

app_name = "main_url_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('accounts/', include("allauth.urls")),
    path('accounts/profile/', workout_views.profile, name="profile"),
    path('accounts/logout/', users_views.logout_user, name="logout_user"),
    path('workout/', include("workout.urls")),
    # path('log-in/', customuser_views.login_current_user, name="login_current_user"),
    # path('log-out/', customuser_views.logout_current_user, name="logout_current_user"),
]
