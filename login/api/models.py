from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager
from django.contrib.auth.models import PermissionsMixin

class CustomUserManager(UserManager):
    def _create_user(self, phn, name, password, **extra_fields):        
        user = self.model(phn=phn, name=name, **extra_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_user(self, phn=None, name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phn, name, password, **extra_fields)
    
    def create_superuser(self, phn=None, name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(phn, name, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    phn = models.IntegerField(primary_key=True, unique=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True)
    username = None

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phn'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.name} {self.phn}'
    
    
# class HealthHistory(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     description = models.TextField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True) 

