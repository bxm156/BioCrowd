from django.conf import settings
from django.contrib.auth import login as django_login
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import resolve_url
from django.shortcuts import render_to_response, RequestContext, redirect
from django.utils.http import is_safe_url
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


from BioCrowd.apps.login.forms import CrispyAuthenticationForm

@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request):
    context = RequestContext(request)
    redirect_to = request.REQUEST.get(REDIRECT_FIELD_NAME, '')

    if request.method == "POST":
        form = CrispyAuthenticationForm(None, request.POST)
        if form.is_valid():
            django_login(request, form.get_user())
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
            return redirect(redirect_to)
    else:
        form = CrispyAuthenticationForm(request)
    context.update({'form': form})
    return render_to_response('login.djhtml', context)