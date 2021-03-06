from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from BioCrowd import settings
from BioCrowd.apps.accounts.common import POSITION_LEVELS, GRADUATE
from BioCrowd.apps.accounts.managers import MyUserManager, WorkerProfileManager
from BioCrowd.apps.universities.models import University

from pycrowd.workers.models import WorkerProfile as pycrowdWorker


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False, editable=False)
    USERNAME_FIELD = 'email'
    
    def get_full_name(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)
    
    def get_short_name(self):
        return self.first_name

    def __unicode__(self):
        return "{first_name} {last_name} ({id})".format(
            first_name=self.first_name,
            last_name=self.last_name,
            id=self.id
        )
    
    objects = MyUserManager()

class WorkerProfile(pycrowdWorker):
    position = models.IntegerField(choices=POSITION_LEVELS, default=GRADUATE)
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="supervisor", null=True, blank=True)
    university = models.ForeignKey(University)

    objects = WorkerProfileManager()