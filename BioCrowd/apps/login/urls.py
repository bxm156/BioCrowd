'''
Created on Nov 1, 2012

@author: Bryan
'''
from django.conf.urls import patterns
from BioCrowd.settings import LOGIN_REDIRECT_URL

urlpatterns = patterns('BioCrowd.apps.login.views',
   #(r'^cas/$','django_cas.views.login',{'next_page':LOGIN_REDIRECT_URL}),
   (r'^$', 'login'),
   #(r'^$', 'login'),
)
