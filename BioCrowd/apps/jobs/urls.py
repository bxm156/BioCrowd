'''
Created on Nov 1, 2012

@author: Bryan
'''
from django.conf.urls import patterns

urlpatterns = patterns('pycrowd.jobs.views',
    (r'^create/$','create',{'template_name':'create.djhtml','extra_context':{'next':'test.html'}}),
)

urlpatterns += patterns('BioCrowd.apps.jobs.views',
    (r'^$', 'home'),
)