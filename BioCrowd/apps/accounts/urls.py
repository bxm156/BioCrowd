'''
Created on Nov 1, 2012

@author: Bryan
'''
from django.conf.urls.defaults import patterns

urlpatterns = patterns('BioCrowd.apps.accounts.views',
   (r'^$', 'home'),
)
