import uuid

from django.db import models

from authentication.models import UserAccount
from backend.settings import MEDIA_ROOT


class UserProfile(models.Model):
    """"
    Class that describes user profile model in database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    user = models.OneToOneField(UserAccount, related_name='user', on_delete=models.CASCADE)
    date_of_birth = models.DateField(default=None, null=True)
    avatar = models.ImageField(upload_to=f'photos/{UserAccount.id}/',
                               default=MEDIA_ROOT + '/userprofile/photos/default.jpg', blank=True, null=True)

    telegram = models.URLField(default=None, null=True)
    facebook = models.URLField(default=None, null=True)
    whatsapp = models.URLField(default=None, null=True)
    twitter = models.URLField(default=None, null=True)
    linkedin = models.URLField(default=None, null=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Профіль користувачів'
        verbose_name_plural = 'Профіль користувачів'
        ordering = ['id']
