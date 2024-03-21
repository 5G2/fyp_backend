from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        
        user.set_password(password)
        user.save()

        return user



class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255,null=True)
    role = models.IntegerField(null=True, default=0)
    gender = models.CharField(null=True, max_length=255)
    phone = models.IntegerField(null=True, default=0)
    create_at=models.DateField(default=timezone.now)
    last_login=models.DateField(default=timezone.now)
    birthday=models.DateField(null=True)
    emergency_contact=models.CharField(null=True,max_length=255)
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','gender','phone']

    def get_username(self):
        return self.username

    def __str__(self):
        return self.email