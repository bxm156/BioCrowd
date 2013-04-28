from django import forms

from BioCrowd import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registration'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = '/account/register/'
        self.helper.add_input(Submit('submit', 'Sign up'))
        
class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
