# Generated by Django 4.1.2 on 2022-10-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealwithclient',
            name='document',
            field=models.ImageField(upload_to='photos/<django.db.models.query_utils.DeferredAttribute object at 0x00000260D545B580>/'),
        ),
        migrations.AlterField(
            model_name='dealwithclient',
            name='genealog',
            field=models.CharField(max_length=255),
        ),
    ]
