# Generated by Django 4.1.2 on 2022-10-27 21:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0023_alter_dealwithclient_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealwithclient',
            name='document',
            field=models.ImageField(blank=True, null=True, upload_to='photos/<django.db.models.query_utils.DeferredAttribute object at 0x00000132DE85F550>/'),
        ),
        migrations.AlterField(
            model_name='dealwithclient',
            name='unique',
            field=models.UUIDField(auto_created=uuid.UUID('90337af0-563c-11ed-bbd1-3ca0670b2ec7'), default=uuid.UUID('90337aef-563c-11ed-98f7-3ca0670b2ec7')),
        ),
    ]