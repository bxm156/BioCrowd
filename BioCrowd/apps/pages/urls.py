'''
Created on Nov 1, 2012

@author: Bryan
'''
from django.conf.urls import patterns

urlpatterns = patterns('BioCrowd.apps.pages.views',
   (r'^$','index'),
)
