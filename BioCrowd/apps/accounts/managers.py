from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, twitter_handle, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=MyUserManager.normalize_email(email),
            twitter_handle=twitter_handle,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user