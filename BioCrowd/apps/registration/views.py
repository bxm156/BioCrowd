# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext

from BioCrowd.apps.registration.forms import UserForm

def register(request):
    context = RequestContext(request)
    if request.method == 'POST':
        data = request.POST.copy()
        form = UserForm(data)
        if form.is_valid():
            user = form.save()
    else:
        form = UserForm()
    context.update({
        'form':form
    })
    return render_to_response('register.djhtml', context)
