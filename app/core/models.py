# database models
from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
    )
class UserManager(BaseUserManager):
    # manager for users
    def create_user(self,email, password = None, **extra_fields):
        # create,save and return a new user
        if not email:
            raise ValueError('User must have an email id.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self,email, password):
        # create and return superuser
        user = self.create_user(email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Recipe(models.Model):
    # Recipe Object
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
