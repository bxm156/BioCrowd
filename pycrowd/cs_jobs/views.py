from django.template.response import TemplateResponse
from pycrowd.cs_jobs.forms import JobForm

def create(request,template_name=None,extra_context=None):
    if request.method == 'POST':
        job_form = JobForm(request.POST)
        job_form.save()
        
    job_form = JobForm()
    context = { 'form': job_form }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request,template_name,context)