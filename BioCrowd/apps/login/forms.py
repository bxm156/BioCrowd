from django.contrib.auth.forms import AuthenticationForm
from django import forms

from crispy_forms.layout import Submit, Layout, Fieldset, Field
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper

class CrispyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label="")
    password = forms.CharField(label="", widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)
    
    def __init__(self, *args, **kwargs):
        super(CrispyAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-login'
        self.helper.form_method = 'post'
        self.helper.form_action = '/login/'
        self.helper.form_tag = False

        self.helper.layout = Layout(
                Field('username', label='', placeholder="Email address", css_class="input-block-level"),
                Field('password', label='', placeholder="Password", css_class="input-block-level"),
                'remember_me',
                Submit('submit', 'Sign in', css_class="btn-large")
        )
        #self.helper.filter(basestring, greedy=True).wrap(Field, css_class="input-xlarge")