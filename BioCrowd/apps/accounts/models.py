from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from BioCrowd import settings
from BioCrowd.apps.accounts.common import POSITION_LEVELS, GRADUATE
from BioCrowd.apps.accounts.managers import MyUserManager
from BioCrowd.apps.universities.models import University


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False, editable=False)
    USERNAME_FIELD = 'email'
    
    def get_full_name(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)
    
    def get_short_name(self):
        return "{first_name}".format(first_name=self.first_name)
    
    def __unicode__(self):
        return "User: {id}".format(id=self.id)
    
    objects = MyUserManager()

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, primary_key=True, editable=False)
    position = models.IntegerField(choices=POSITION_LEVELS, default=GRADUATE)
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="supervisor", null=True, blank=True)
    university = models.ForeignKey(University)