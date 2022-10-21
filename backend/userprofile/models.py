from django.db import models

from authentication.models import UserAccount
from backend.settings import MEDIA_ROOT


class UserProfile(models.Model):
    """"
    Class that describes user profile model in database
    """
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default=None, null=True)
    avatar = models.ImageField(upload_to=f'photos/{UserAccount.uid}/',
                               default=MEDIA_ROOT + '/userprofile/photos/default.jpg')

    telegram = models.URLField(default=None, null=True)
    facebook = models.URLField(default=None, null=True)
    whatsapp = models.URLField(default=None, null=True)
    twitter = models.URLField(default=None, null=True)
    linkedin = models.URLField(default=None, null=True)
