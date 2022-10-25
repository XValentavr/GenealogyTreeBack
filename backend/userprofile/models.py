from django.db import models

from authentication.models import UserAccount


class UserProfile(models.Model):
    """"
    Class that describes user profile model in database
    """
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default=None, null=True)
    avatar = models.ImageField(upload_to=f'photos/{UserAccount.uid}/',blank=True, null=True)

    telegram = models.URLField(default=None, null=True)
    facebook = models.URLField(default=None, null=True)
    whatsapp = models.URLField(default=None, null=True)
    twitter = models.URLField(default=None, null=True)
    linkedin = models.URLField(default=None, null=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профиль пользователя'
        ordering = ['id']
