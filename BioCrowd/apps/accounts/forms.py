from django import forms
from BioCrowd.apps.accounts.models import UserProfile

class UserProfile(forms.ModelForm):
    
    class Meta:
        model = UserProfile