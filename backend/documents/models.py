from django.db import models


# Create your models here.
class Documents(models.Model):
    """
    represent male line chile
    """
    url = models.URLField(default=None, null=True)
