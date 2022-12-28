import uuid

from django.db import models

from authentication.models import UserAccount
from userprofile.models import UserProfile


# Create your models here.
class GenealogistBuildsTree(models.Model):
    """
    Creates table of info about building trees by genealogist
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    client = models.ForeignKey(UserAccount, on_delete=models.CASCADE, unique=False, related_name='client')
    isShown = models.BooleanField(default=False, null=True)
    genealogist = models.ForeignKey(UserAccount, null=True, on_delete=models.CASCADE, unique=False,
                                    related_name='genealogist')

    def __str__(self):
        return self.client.user.username

    class Meta:
        verbose_name = 'Дерево клієнта'
        verbose_name_plural = 'Дерево клієнта'
        ordering = ['id']
