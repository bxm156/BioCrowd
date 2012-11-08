'''
Created on Nov 6, 2012

@author: Bryan
'''
from django.db import models
from csengine.hits.models import HumanTask

class Question(models.Model):
    hit = models.ManyToOneRel(HumanTask)
    question = models.CharField(max_length=30)
    image = models.URLField()
    
    class Meta:
        abstract = True

class Answer(models.Model):
    text = models.CharField(max_length=30)
        
class MultipleChoiceQuestion(Question):
    choices = models.ManyToManyField(Answer)
    