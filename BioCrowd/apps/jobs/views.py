from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required

from BioCrowd.apps.jobs.forms import CrispyCrowdsourceJobForm


def home(request):
    return render(request,'home.djhtml')

@login_required
def create(request):
    context = RequestContext(request)
    form = CrispyCrowdsourceJobForm()
    context.update({'form': form})
    return render_to_response('create.djhtml', context)