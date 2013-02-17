'''
Created on Nov 6, 2012

@author: Bryan
'''
from django.db import models
import pycrowd.settings as settings

class CrowdsourceJob(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.PROFILE_MODULE,editable=False)
    instructions = models.TextField()
    target_accuracy = models.IntegerField()
    task_count = models.IntegerField(editable=False)