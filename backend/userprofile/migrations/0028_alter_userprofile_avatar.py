# Generated by Django 4.1.2 on 2022-10-27 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0027_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='D:\\Metrics\\GenealogyBoutiqueTree\\backend\\media/userprofile/photos/default.jpg', null=True, upload_to='photos/<django.db.models.query_utils.DeferredAttribute object at 0x000001DB4E454190>/'),
        ),
    ]