'''
Created on Nov 1, 2012

@author: Bryan
'''
from django.conf.urls import patterns

urlpatterns = patterns('BioCrowd.apps.registration.views',
    (r'^register/$','register'),
)
