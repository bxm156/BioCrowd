'''
Created on Nov 6, 2012

@author: Bryan
'''
from django.db import models
import pycrowd.settings as settings

class WorkerProfile(models.Model):
    user = models.ForeignKey(settings.PROFILE_MODULE)
    trust_level = models.PositiveSmallIntegerField(default=5)
    
    