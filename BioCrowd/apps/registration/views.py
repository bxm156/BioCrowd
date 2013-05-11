# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.shortcuts import RequestContext

from BioCrowd.apps.registration.forms import UserForm, UserProfileForm

def register(request):
    context = RequestContext(request)
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user = authenticate(username=user.email, password=form.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                print "You provided a correct username and password!"
                login(request, user)
                return redirect('/account/register/profile')
            else:
                print "Your account has been disabled!"
        else:
            print "Your username and password were incorrect."
    context.update({'form':form})
    return render_to_response('register.djhtml', context)

def activate(request, user_id, key):
    pass
    
@login_required
def profile(request):
    context = RequestContext(request)
    form = UserProfileForm(request.POST,user=request.user)
    if form.is_valid():
        form.save()
        return redirect("/account/")
    context.update({'form':form})
    return render_to_response('register.djhtml', context)