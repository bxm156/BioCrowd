from django.contrib.auth.models import BaseUserManager
from django.db.models import Manager

class MyUserManager(BaseUserManager):
    use_for_related_fields = True
    
    def create_user(self, email, password=None, is_active=False, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=email,
            is_active=is_active,
            **extra_fields
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class WorkerProfileManager(Manager):
    use_for_related_fields = True
    
    def create_worker_profile(self, user, trust_level, position, supervisor, university, **extra_fields):
        
        profile = self.model(
           user=user,
           trust_level=trust_level,
           position=position,
           supervisor=supervisor,
           university=university,
           **extra_fields
        )
        profile.save(using=self._db)
        return profile