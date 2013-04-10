'''
Created on Nov 1, 2012

@author: Bryan
'''
from django.conf.urls import patterns

urlpatterns = patterns('BioCrowd.apps.accounts.views',
    (r'^profile/$','profile'),
    (r'^logout/$','logout'),
    (r'^$', 'home'),
)
