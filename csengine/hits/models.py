'''
Created on Nov 7, 2012

@author: Bryan
'''
from django.db import models
import csengine.settings as settings
import csengine.query.models

class HumanTask(models.Model):
    worker = models.ForeignKey(settings.WORKER_PROFILE)
    completed = models.BooleanField()
    date_finished = models.DateTimeField()
    
    def getQuestion(self):
        return csengine.query.models.MultipleChoiceQuestion.objects.get(hit=id)
        