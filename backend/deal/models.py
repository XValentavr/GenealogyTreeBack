import uuid

from django.db import models

from authentication.models import UserAccount
from userprofile.models import UserProfile


# Create your models here.
class DealWithClient(models.Model):
    """
    Creates table of info abount user and deal
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    clientTree = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE, unique=False,
                                   related_name='clientTree')
    date = models.DateField(null=True)
    document = models.ImageField(upload_to=f'photos/{UserAccount.id}/', blank=True, null=True)
    context = models.TextField(null=True)
    is_published = models.BooleanField(default=False)
    genealogistTree = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE, null=True, unique=False,
                                        related_name='genealogistTree')

    def __str__(self):
        return self.clientTree.user.email

    class Meta:
        verbose_name = 'Угоди'
        verbose_name_plural = 'Угоди'
        ordering = ['id']
