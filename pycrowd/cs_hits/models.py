'''
Created on Nov 7, 2012

@author: Bryan
'''
from django.db import models
import pycrowd.settings as settings
import pycrowd.cs_query.models

class HumanTask(models.Model):
    worker = models.ForeignKey(settings.WORKER_PROFILE)
    completed = models.BooleanField()
    date_finished = models.DateTimeField()
    
    def getQuestion(self):
        return pycrowd.cs_query.models.MultipleChoiceQuestion.objects.get(hit=id)
        