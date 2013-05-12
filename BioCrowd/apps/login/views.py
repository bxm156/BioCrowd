from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render_to_response, RequestContext, redirect

from BioCrowd.apps.login.forms import CrispyAuthenticationForm

def login(request):
    context = RequestContext(request)
    if request.method == "POST":
        form = CrispyAuthenticationForm(request, request.POST)
        if form.is_valid():
            django_login(request, form.get_user())
            return redirect("/account/")
    else:
        form = CrispyAuthenticationForm(request)
    context.update({'form': form})
    return render_to_response('login.djhtml', context)