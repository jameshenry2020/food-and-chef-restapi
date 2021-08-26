from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email=models.EmailField(verbose_name="Email Address", max_length=255, unique=True)
    is_chef=models.BooleanField(default=False)


    REQUIRED_FIELDS=['username','first_name','last_name']
    USERNAME_FIELD='email'

    def get_username(self):
        return self.email


class Profile(models.Model):
    bio=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to='profile', blank=True, null=True)
    phone=models.CharField(max_length=15, blank=True, null=True)
    country=models.CharField(max_length=200, blank=True, null=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ChefBook(models.Model):
    name=models.CharField(max_length=100)
    chef=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name