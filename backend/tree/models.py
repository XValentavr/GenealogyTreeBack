import uuid
from django.db import models

from authentication.models import UserAccount
from documents.models import Documents


# Create your models here.
class MainRootUser(models.Model):
    """
    This class creates database root user
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    surname = models.CharField(max_length=255, null=True)
    mother_surname = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(default=None, null=True)
    place_of_birth = models.CharField(max_length=255, null=True)
    date_of_marry = models.DateField(default=None, null=True)
    is_dead = models.BooleanField(default=False)
    date_of_death = models.DateField(default=None, null=True)
    years = models.CharField(max_length=255, default=None, null=True)

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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
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
    email = models.EmailField(null=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, unique=False)
    sex = models.CharField(max_length=10, null=False, default='М')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дружина'
        ordering = ['id']


class MainRootUserSpouse(models.Model):
    """
    This class creates database root user spouse
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
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
    email = models.EmailField(null=True)
    sex = models.CharField(max_length=10, null=False, default='М')
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    root = models.ForeignKey(MainRootUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    mother_surname = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(default=None, null=True)
    place_of_birth = models.CharField(max_length=255, null=True)
    date_of_marry = models.DateField(default=None, null=True)
    date_of_death = models.DateField(default=None, null=True)
    document = models.ForeignKey(Documents, null=True, on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=False)
    sex = models.CharField(max_length=10, null=False, default='Ж')
    prev_ancestor = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.surname

    class Meta:
        verbose_name = 'Інформація по жіночій лінії'
        verbose_name_plural = 'Інформація по жіночій лінії'


class MaleLine(models.Model):
    """
    represent male line
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    root = models.ForeignKey(MainRootUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    mother_surname = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(default=None, null=True)
    place_of_birth = models.CharField(max_length=255, null=True)
    date_of_marry = models.DateField(default=None, null=True)
    date_of_death = models.DateField(default=None, null=True)
    document = models.ForeignKey(Documents, null=True, on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=False)
    sex = models.CharField(max_length=10, null=False, default='М')
    prev_ancestor = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.surname

    class Meta:
        verbose_name = 'Інформація по чоловічій лінії'
        verbose_name_plural = 'Інформація по чоловічій лінії'


class FemaleLineChild(models.Model):
    """
    represent female line child
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    root = models.ForeignKey(MainRootUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    mother_surname = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(default=None, null=True)
    place_of_birth = models.CharField(max_length=255, null=True)
    date_of_marry = models.DateField(default=None, null=True)
    date_of_death = models.DateField(default=None, null=True)
    document = models.ForeignKey(Documents, null=True, on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=False)
    sex = models.CharField(max_length=10, null=False, default='М')
    next_ancestor = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.surname

    class Meta:
        verbose_name = 'Інформація по чоловічій лінії'
        verbose_name_plural = 'Інформація по чоловічій лінії'


class MaleLineChild(models.Model):
    """
    represent male line chile
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    root = models.ForeignKey(MainRootUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    mother_surname = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(default=None, null=True)
    place_of_birth = models.CharField(max_length=255, null=True)
    date_of_marry = models.DateField(default=None, null=True)
    date_of_death = models.DateField(default=None, null=True)
    document = models.ForeignKey(Documents, null=True, on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=False)
    sex = models.CharField(max_length=10, null=False, default='Ж')
    next_ancestor = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.surname

    class Meta:
        verbose_name = 'Інформація про дітей по чоловічій лінії'
        verbose_name_plural = 'Інформація про дітей по чоловічій лінії'
