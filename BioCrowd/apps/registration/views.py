# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext

from BioCrowd.apps.registration.forms import UserForm, UserRegistrationForm

def register(request):
    context = RequestContext(request)
    if request.method == 'POST':
        data = request.POST.copy()
        form = UserForm(data)
        if form.is_valid():
            pass
    else:
        form = UserForm()
        context.update({
            #'errors':registration.errors,
            'form':form
        })
    return render_to_response('register.djhtml', context)
