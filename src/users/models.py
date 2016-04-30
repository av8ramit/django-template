'''Models page for the users django template module.'''

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from .utils import upload_location


class MyUserManager(BaseUserManager):
    '''Model manager for the MyUser class.'''

    def create_user(self, username=None, email=None, password=None):
        '''Creates and saves a User with the given username, email and password.'''

        if not username:
            raise ValueError('Must include username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        '''Creates and saves a superuser with the given username, email and password.'''

        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    '''Base model custom User class for authentication.'''

    username = models.CharField(
        max_length=255,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )
    is_member = models.BooleanField(
        default=False,
        verbose_name='Is Paid Member'
    )
    image = models.FileField(
        upload_to=upload_location,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        '''The user is identified by their email address.'''
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        '''The user is identified by their email address.'''
        if self.first_name:
            return self.first_name
        else:
            return self.username

    def __unicode__(self):
        '''Return the username as the string representation.'''
        return self.username

    def has_module_perms(self, app_label):
        '''Does the user have permissions to view the app `app_label`?'''
        return self.is_active

    def has_perm(self, app_label):
        '''Does the user have permissions to view the app `app_label`?'''
        return self.is_active

    def has_image(self):
        '''Does the user have a profile image?'''
        return self.image.name

    @property
    def is_staff(self):
        '''Is the user a member of staff?'''
        return self.is_admin
