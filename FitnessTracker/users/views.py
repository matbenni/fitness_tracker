from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

# Create your views here.
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")