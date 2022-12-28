import uuid

from django.db import models


# Create your models here.


class Support(models.Model):
    """
    Represent tech support
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=255, null=False)
    context = models.TextField(null=False)
    date = models.DateField(null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Технічна підтримка'
        verbose_name_plural = 'Технічна підтримка'
        ordering = ['id']
