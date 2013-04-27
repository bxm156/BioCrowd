from django import forms

from BioCrowd import settings
from BioCrowd.apps.accounts.models import UserProfile

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        
class UserForm(forms.Form):
    
    class Meta:
        model = settings.AUTH_USER_MODEL
        
class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=254)
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()