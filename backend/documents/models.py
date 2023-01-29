import uuid

from django.db import models


# Create your models here.
class Documents(models.Model):
    """
    represent male line chile
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    url = models.URLField(default=None, null=True)