from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from allauth.account.views import SignupView
from allauth.account import app_settings

# Create your views here.
class CustomSignupView(SignupView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_message'] = "Join thousands and start your fitness journey today!"
        return context

    def form_valid(self, form):
        
        response = super().form_valid(form)

        if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
            messages.info(self.request, "Please verify your account via the email we sent you.")
        else:
            messages.success(self.request, f"Welcome {form.cleaned_data['first_name']}! Your account has been created.")
        return response

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")