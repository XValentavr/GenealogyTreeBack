import uuid

from django.db import models

from authentication.models import UserAccount


# Create your models here.
class MainRootUser(models.Model):
    """
    This class creates database root user
    """
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    surname = models.CharField(max_length=255, null=True)
    mother_surname = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(default=None, null=True)
    place_of_birth = models.CharField(max_length=255, null=True)
    date_of_marry = models.DateField(default=None, null=True)
    unique_root = models.UUIDField(default=uuid.uuid1())

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Информация о корне дерева'
        verbose_name_plural = 'Информация о корне дерева'
        ordering = ['id']


class FemaleLine(models.Model):
    """
    Resresents female line
    """
    root = models.ForeignKey(MainRootUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    mother_surname = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(default=None, null=True)
    place_of_birth = models.CharField(max_length=255, null=True)
    date_of_marry = models.DateField(default=None, null=True)
    date_of_death = models.DateField(default=None, null=True)
    document = models.ImageField(upload_to=f'tree/{UserAccount.uid}/female', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    unique_female = models.UUIDField(default=uuid.uuid1())

    def __str__(self):
        return self.first_name + ', ' + self.last_name + ', ' + self.surname

    class Meta:
        verbose_name = 'Информация о листьях дерева по женской линии'
        verbose_name_plural = 'Информация о листьях дерева по женской линии'


class MaleLine(models.Model):
    """
    represent male line
    """
    root = models.ForeignKey(MainRootUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    mother_surname = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(default=None, null=True)
    place_of_birth = models.CharField(max_length=255, null=True)
    date_of_marry = models.DateField(default=None, null=True)
    date_of_death = models.DateField(default=None, null=True)
    document = models.ImageField(upload_to=f'tree/{UserAccount.uid}/male', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    unique_male = models.UUIDField(default=uuid.uuid1())

    def __str__(self):
        return self.first_name + ', ' + self.last_name + ', ' + self.surname

    class Meta:
        verbose_name = 'Информация о корне дерева по мужской линии'
        verbose_name_plural = 'Информация о корне дерева по мужской линии'
