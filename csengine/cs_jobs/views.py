from django.template.response import TemplateResponse

def create(request,template_name=None):
    return TemplateResponse(request,template_name)