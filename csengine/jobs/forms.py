
from django import forms
from csengine.jobs.models import CrowdsourceJob

class JobForm(forms.ModelForm):
    
    class Meta:
        model = CrowdsourceJob
    