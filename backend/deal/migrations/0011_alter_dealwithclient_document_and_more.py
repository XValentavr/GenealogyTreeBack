# Generated by Django 4.1.2 on 2022-10-25 13:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0010_alter_dealwithclient_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealwithclient',
            name='document',
            field=models.ImageField(blank=True, null=True, upload_to='photos/<django.db.models.query_utils.DeferredAttribute object at 0x0000020E7E5DB580>/'),
        ),
        migrations.AlterField(
            model_name='dealwithclient',
            name='unique',
            field=models.UUIDField(auto_created=uuid.UUID('1a7ee8bb-5466-11ed-868c-2c4d54929b0f'), default=uuid.UUID('1a7ee8ba-5466-11ed-92a8-2c4d54929b0f')),
        ),
    ]