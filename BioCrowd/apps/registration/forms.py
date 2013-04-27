from django import forms

from BioCrowd import settings
from BioCrowd.apps.accounts.models import UserProfile, User

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'confirm_password', )
        #exclude = ('last_login',)
        
class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
