'''
Created on Nov 7, 2012

@author: Bryan
'''
from django.db import models
import csengine.settings as settings
from csengine.query.models import MultipleChoiceQuestion

class HumanTask(models.Model):
    worker = models.ForeignKey(settings.WORKER_PROFILE)
    
    def getQuestion(self):
        return MultipleChoiceQuestion.objects.filter(hit=id)
        