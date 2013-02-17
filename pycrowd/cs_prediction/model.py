'''
Created on Nov 6, 2012

@author: Bryan
'''
import pycrowd.settings as settings
from pycrowd.cs_jobs.plan import JobPlan
from django.db.models import get_model

class PredictionModel():
    
    def __init__(self,job_model):
        self.job = job_model
        self.worker_profile = get_model(*settings.WORKER_PROFILE.split('.',1))
        self.worker_manager = self.worker_profile._default_manager
    
    def get_worker_count(self):
        raise("Not Implemented")
    
    def get_worker_ids(self):
        return None
    
    def get_plan(self):
        return JobPlan()
    


class SimplePredictionModel(PredictionModel):
    
    def get_worker_count(self):
        return 1
    
    def get_worker_ids(self):
        return [self.worker_manager.order_by('-trust_level')[0:1].get().id]
    
    def get_plan(self):
        return JobPlan(self.get_worker_ids(),self.job.task_count)