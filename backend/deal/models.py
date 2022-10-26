import uuid

from django.db import models

from authentication.models import UserAccount
from userprofile.models import UserProfile


# Create your models here.
class DealWithClient(models.Model):
    """
    Creates table of info abount user and deal
    """
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, unique=False, related_name='client')
    date = models.DateField(null=True)
    document = models.ImageField(upload_to=f'photos/{UserAccount.uid}/', blank=True, null=True)
    context = models.TextField(null=True)
    is_published = models.BooleanField(default=False)
    genealog = models.CharField(max_length=255, null=True)
    unique = models.UUIDField(default=uuid.uuid1(), auto_created=uuid.uuid1())

    def __str__(self):
        return self.client.user.email

    class Meta:
        verbose_name = 'Угоди'
        verbose_name_plural = 'Угоди'
        ordering = ['id']
