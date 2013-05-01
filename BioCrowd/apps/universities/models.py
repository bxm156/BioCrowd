from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=9)
    url = models.URLField()
    
    class Meta:
        unique_together= ('name', 'address', 'city', 'state', 'zipcode' ,'url')
        
    def __unicode__(self):
        return "{school}, {city}, {state}".format(
            school=self.name,
            city=self.city,
            state=self.state
        )