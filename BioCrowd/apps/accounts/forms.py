from django import forms
from BioCrowd.apps.accounts.models import UserProfile

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile