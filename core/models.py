import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, \
    BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


class UserManager(BaseUserManager):
    """ Customer user manager """
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Username can't be blank")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if not username:
            raise ValueError("Username can't be blank")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return self.create_user(username=username, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ Customer user class"""
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(max_length=100, null=True)

    objects = UserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


def recipe_upload_file_path(instance, filename):
    """ Generate file path for recipe banner """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('uploads/recipe', filename)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=recipe_upload_file_path)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe_name

