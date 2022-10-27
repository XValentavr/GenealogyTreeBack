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
    is_dead = models.BooleanField(default=False)
    date_of_death = models.DateField(default=None, null=True)
    years = models.CharField(max_length=255, default=None, null=True)
    unique_root = models.UUIDField(default=uuid.uuid1())

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Корінь дерева'
        verbose_name_plural = 'Корінь дерева'
        ordering = ['id']


class MainRootUserWife(models.Model):
    """
    This class creates database root user wife
    """
    spouse = models.ForeignKey(MainRootUser, on_delete=models.CASCADE, unique=False)
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    mother_surname = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(default=None, null=True)
    place_of_birth = models.CharField(max_length=255, null=True)
    date_of_marry = models.DateField(default=None, null=True)
    is_dead = models.BooleanField(default=False)
    date_of_death = models.DateField(default=None, null=True)
    years = models.CharField(max_length=255, default=None, null=True)
    unique_root = models.UUIDField(default=uuid.uuid1())
    email = models.EmailField(null=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, unique=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дружина'
        ordering = ['id']


class MainRootUserSpouse(models.Model):
    """
    This class creates database root user spouse
    """
    wife = models.ForeignKey(MainRootUser, on_delete=models.CASCADE, unique=False)
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    mother_surname = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(default=None, null=True)
    place_of_birth = models.CharField(max_length=255, null=True)
    date_of_marry = models.DateField(default=None, null=True)
    is_dead = models.BooleanField(default=False)
    date_of_death = models.DateField(default=None, null=True)
    years = models.CharField(max_length=255, default=None, null=True)
    unique_root = models.UUIDField(default=uuid.uuid1())
    email = models.EmailField(null=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, unique=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Чоловік'
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
        return self.first_name + ' ' + self.last_name + ' ' + self.surname

    class Meta:
        verbose_name = 'Інформація по жіночій лінії'
        verbose_name_plural = 'Інформація по жіночій лінії'


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
        return self.first_name + ' ' + self.last_name + ' ' + self.surname

    class Meta:
        verbose_name = 'Інформація по чоловічій лінії'
        verbose_name_plural = 'Інформація по чоловічій лінії'
