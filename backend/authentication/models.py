import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager


class UserAccountManager(UserManager):
    def create_user(self, username, is_genealogist, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, is_genealogist=is_genealogist)
        user.set_password(password)
        user.save()

        create_user_profile(user=user)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, is_staff=True, is_active=True, is_superuser=True)
        user.set_password(password)
        user.save()

        create_user_profile(user=user)

        return user


class UserAccount(AbstractUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_genealogist = models.BooleanField(default=False)
    objects = UserAccountManager()
    sex = models.CharField(max_length=10, default=None, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'is_genealogist']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Користувачі'
        verbose_name_plural = 'Користувачі'
        ordering = ['id']


def create_user_profile(user):
    """
    Function creates user account
    """
    from userprofile.models import UserProfile
    userprofile = UserProfile(user=user, user_id=user.pk)
    userprofile.save()

    from tree.models import MainRootUser
    root_user = MainRootUser(rootUser=user, rootUser_id=user.pk, buildsBy=None)
    root_user.save()
