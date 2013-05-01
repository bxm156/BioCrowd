import string
import random

from django.db import models

from BioCrowd import settings

# Create your models here.
class UserActivation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    activation_key = models.CharField(max_length=30)
    
    def get_random_key(self, size=30, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    
    @models.permalink
    def get_absolute_url(self):
        return ('BioCrowd.apps.registration.views.view', [str(self.event.id)])
    def get_url(self, user):
        return '/account/registration/activate/{user_id}/{key}'.format(user_id=self.id, key=self.activation_key)