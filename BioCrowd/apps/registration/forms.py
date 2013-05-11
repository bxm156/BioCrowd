from django import forms

from BioCrowd import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field
from crispy_forms.bootstrap import FormActions
from BioCrowd.apps.accounts.models import WorkerProfile, User

from pycrowd.workers.forms import WorkerForm as pycrowdWorkerForm


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
        #self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/account/register/'
        #self.helper.add_input(Submit('submit', 'Sign up'))
        self.helper.layout = Layout(
            Fieldset(
                'Sign up',
                'first_name',
                'last_name',
                'email',
                'password',
                'confirm_password'
            ),
            FormActions(
                Submit('submit', 'Signup', css_class="btn-large")
            )
        )
        self.helper.filter(basestring, greedy=True).wrap(Field, css_class="input-xlarge")
        
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
    
        if not confirm_password:
            raise forms.ValidationError("You must confirm your password")
        if password != confirm_password:
            raise forms.ValidationError("Your passwords do not match")
        return confirm_password
    
    def save(self):
        new_user = User.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data.get('password'),
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            is_active=True,
        )
        new_user.save()
        return new_user


class UserProfileForm(pycrowdWorkerForm):
    
    class Meta:
        model = WorkerProfile
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UserProfileForm, self).__init__(*args, **kwargs)
 
        self.helper = FormHelper()
        self.helper.form_id = 'id-user-profile'
        #self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/account/register/profile/'
        self.helper.add_input(Submit('submit', 'Complete'))
        
    def save(self):
        assert(self.user)
        return WorkerProfile.objects.create_worker_profile(
            user=self.user,
            trust_level=0,
            position=self.cleaned_data['position'],
            supervisor=self.cleaned_data['supervisor'],
            university=self.cleaned_data['university']
        )
        
