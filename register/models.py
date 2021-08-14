from django.db import models

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.email



class Dieter(models.Model):
    username = models.CharField(max_length=10)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile = models.TextField()
    address = models.TextField()


class Gym(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gym_name = models.CharField(max_length=100)
    address = models.TextField()
    logo = models.TextField()
    website = models.URLField()
    profile1 = models.TextField()
    profile2 = models.TextField()
    profile3 = models.TextField()
    clients = models.ManyToManyField(Dieter,related_name='coaches')
    price_desc = models.TextField()