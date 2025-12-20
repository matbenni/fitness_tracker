from django import forms
from users.models import UserProfile

# This CustomSignupForm edits the django-allauth signup form by adding fields for your custom user model
class CustomSignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder':'First Name'})
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder':'Last Name'})
    )
    birth_date = forms.DateField(
        input_formats=('%Y/%m/%d', '%Y-%m-%d', '%m/%d/%Y', '%m-%d-%Y'),
        widget=forms.TextInput(attrs={'type':'date'})
    )
    phone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'Phone Number'})
    )
    height_feet = forms.IntegerField(
        max_value=99,
        widget=forms.TextInput(attrs={'placeholder':'Height (Feet)'})
    )
    height_inches = forms.DecimalField(
        max_value=11.99,
        decimal_places=2,
        widget=forms.TextInput(attrs={'placeholder':'Height (Inches)'})
    )
    weight_lbs = forms.IntegerField(
        max_value=999,
        widget=forms.TextInput(attrs={'placeholder':'Weight (lbs)'})
    )

    def signup(self, request, user):
        # This will save the user and create the user ID associated with the django user model
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Create the User Profile associate with the django user model user
        profile = UserProfile(user=user)
        profile.birth_date = self.cleaned_data.get('birth_date', '')
        profile.phone = self.cleaned_data.get('phone', '')
        profile.height_feet = self.cleaned_data.get('height_feet', '')
        profile.height_inches = self.cleaned_data.get('height_inches', '')
        profile.weight_lbs = self.cleaned_data.get('weight_lbs', '')
        profile.save()
