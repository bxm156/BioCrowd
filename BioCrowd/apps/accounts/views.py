# Create your views here.

from django.shortcuts import render_to_response, redirect
from django.shortcuts import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as djangoLogout

@login_required
def home(request):
    context = RequestContext(request)
    return render_to_response('home.djhtml', context)

def logout(request):
    if request.user.is_authenticated():
        djangoLogout(request)
    return redirect("/")