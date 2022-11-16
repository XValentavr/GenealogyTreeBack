# Generated by Django 4.1.2 on 2022-10-27 15:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0015_alter_dealwithclient_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealwithclient',
            name='document',
            field=models.ImageField(blank=True, null=True, upload_to='photos/<django.db.models.query_utils.DeferredAttribute object at 0x00000270DE7F4190>/'),
        ),
        migrations.AlterField(
            model_name='dealwithclient',
            name='unique',
            field=models.UUIDField(auto_created=uuid.UUID('d697d508-560d-11ed-9be1-3ca0670b2ec7'), default=uuid.UUID('d697ac0f-560d-11ed-989d-3ca0670b2ec7')),
        ),
    ]
