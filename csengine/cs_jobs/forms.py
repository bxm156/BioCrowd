
from django import forms
from csengine.cs_jobs.models import CrowdsourceJob

class JobForm(forms.ModelForm):
    
    class Meta:
        model = CrowdsourceJob
    