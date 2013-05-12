from django.conf import settings

def site_title(request):
    context = {'SITE_TITLE': settings.SITE_TITLE}
    if request.user.is_authenticated():
        context.update({'USERNAME': request.user.email})
    return context