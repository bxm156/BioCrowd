# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as djangoLogout

def home(request):
    return render(request,'account.djhtml')

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST,instance=request.user.get_profile())
        if profile_form.is_valid():
            profile_form.save()
        return render(request,'profile.djhtml', {'profile_form':profile_form})
    else:
        profile = request.user.get_profile()
        profile_form = UserProfileForm(instance=profile)
        return render(request, 'profile.djhtml', {'profile_form':profile_form})
    
def logout(request):
    if request.user.is_authenticated():
        djangoLogout(request)
    return redirect("/")