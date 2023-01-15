import uuid
from django.db import models

from authentication.models import UserAccount
from documents.models import Documents
from genealogistBuildsTree.models import GenealogistBuildsTree


class AnyTreeInfo(models.Model):
    """
    This class creates database base info about any part of tree
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)

    firstName = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    lastName = models.CharField(max_length=255, null=True)
    motherSurname = models.CharField(max_length=255, null=True)
    dateOfBirth = models.DateField(default=None, null=True)
    placeOfBirth = models.CharField(max_length=255, null=True)
    dateOfMarry = models.DateField(default=None, null=True)
    dateOfDeath = models.DateField(default=None, null=True)
    placeOfDeath = models.CharField(max_length=255, null=True)
    reasonOfDeath = models.CharField(max_length=255, null=True)

    document = models.ForeignKey(Documents, null=True, on_delete=models.SET_NULL)
    isPublished = models.BooleanField(default=False)
    sex = models.CharField(max_length=10, null=True)
    isConfidential = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Корінь дерева'
        verbose_name_plural = 'Корінь дерева'
        ordering = ['id']


# Create your models here.
class MainRootUser(models.Model):
    """
    This class creates database root user
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    rootUser = models.OneToOneField(UserAccount, null=True, on_delete=models.CASCADE)
    anyInfo = models.ForeignKey(AnyTreeInfo, null=True, related_name='allInfo', on_delete=models.SET_NULL)

    buildsBy = models.ForeignKey(GenealogistBuildsTree, default=None, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.rootUser.username

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
    anyInfo = models.ForeignKey(AnyTreeInfo, null=True, on_delete=models.SET_NULL)

    email = models.EmailField(null=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, unique=False)

    def __str__(self):
        return self.anyInfo.firstName

    class Meta:
        verbose_name = 'Дружина'
        ordering = ['id']


class MainRootUserSpouse(models.Model):
    """
    This class creates database root user spouse
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    wife = models.ForeignKey(MainRootUser, on_delete=models.CASCADE, unique=False)
    anyInfo = models.ForeignKey(AnyTreeInfo, null=True, on_delete=models.SET_NULL)

    email = models.EmailField(null=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, unique=False)

    def __str__(self):
        return self.anyInfo.firstName

    class Meta:
        verbose_name = 'Чоловік'
        ordering = ['id']


class FemaleLine(models.Model):
    """
    Resresents female line
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    root = models.ForeignKey(MainRootUser, on_delete=models.CASCADE)
    anyInfo = models.ForeignKey(AnyTreeInfo, null=True, on_delete=models.SET_NULL)

    prevAncestor = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.anyInfo.firstName + ' ' + self.anyInfo.lastName + ' ' + self.anyInfo.surname

    class Meta:
        verbose_name = 'Інформація по жіночій лінії'
        verbose_name_plural = 'Інформація по жіночій лінії'


class MaleLine(models.Model):
    """
    represent male line
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    root = models.ForeignKey(MainRootUser, on_delete=models.CASCADE)
    anyInfo = models.ForeignKey(AnyTreeInfo, null=True, on_delete=models.SET_NULL)

    prevAncestor = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.anyInfo.firstName + ' ' + self.anyInfo.lastName + ' ' + self.anyInfo.surname

    class Meta:
        verbose_name = 'Інформація по чоловічій лінії'
        verbose_name_plural = 'Інформація по чоловічій лінії'


class FemaleLineChild(models.Model):
    """
    represent female line child
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    root = models.ForeignKey(MainRootUser, on_delete=models.CASCADE)
    anyInfo = models.ForeignKey(AnyTreeInfo, null=True, on_delete=models.SET_NULL)

    nextAncestor = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.anyInfo.firstName + ' ' + self.anyInfo.lastName + ' ' + self.anyInfo.surname

    class Meta:
        verbose_name = 'Інформація по чоловічій лінії'
        verbose_name_plural = 'Інформація по чоловічій лінії'


class MaleLineChild(models.Model):
    """
    represent male line chile
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    root = models.ForeignKey(MainRootUser, on_delete=models.CASCADE)
    anyInfo = models.ForeignKey(AnyTreeInfo, null=True, on_delete=models.SET_NULL)

    nextAncestor = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.anyInfo.firstName + ' ' + self.anyInfo.lastName + ' ' + self.anyInfo.surname

    class Meta:
        verbose_name = 'Інформація про дітей по чоловічій лінії'
        verbose_name_plural = 'Інформація про дітей по чоловічій лінії'
