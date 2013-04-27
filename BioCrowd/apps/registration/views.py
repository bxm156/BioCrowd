# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext

from BioCrowd.apps.registration.forms import UserForm, UserRegistrationForm

def register(request):
    form = UserRegistrationForm()
    context = RequestContext(request, {
        #'errors':registration.errors,
        'form':form
    })
    return render_to_response('register.djhtml', context)
