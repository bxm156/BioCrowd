'''
Created on Nov 6, 2012

@author: Bryan
'''

class JobPlan():
    
    def __init__(self,workers=None,workload=-1):
        self.workers = workers
        self.workload = workload