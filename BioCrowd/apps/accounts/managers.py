from django.contrib.auth.models import BaseUserManager


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