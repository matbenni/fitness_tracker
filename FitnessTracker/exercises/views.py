from django.shortcuts import render

# Create your views here.
def user_exercises_list(request):
    return render(request, "exercises_list.html")