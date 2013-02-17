
from django import forms
from pycrowd.cs_jobs.models import CrowdsourceJob

class JobForm(forms.ModelForm):
    
    class Meta:
        model = CrowdsourceJob
    