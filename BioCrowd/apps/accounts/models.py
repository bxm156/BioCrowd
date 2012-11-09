from django.db import models
from django.contrib.auth.models import User
# Create your models here.


EXPERT = 4
PROFESSOR = 3
GRADUATE = 2
UNDERGRADUATE = 1
POSITION_LEVELS = (
                   (EXPERT,"Expert"),
                   (PROFESSOR,"Professsor"),
                   (GRADUATE,"Graduate Student"),
                   (UNDERGRADUATE,"Undergraduate Student")
                   )

class UserProfile(models.Model):
    user = models.ForeignKey(User, primary_key=True, editable=False)
    position = models.IntegerField(choices=POSITION_LEVELS,default=PROFESSOR)
    supervisor = models.ForeignKey(User,related_name="supervisor",null=True)
    