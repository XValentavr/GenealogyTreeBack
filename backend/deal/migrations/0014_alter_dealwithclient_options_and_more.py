# Generated by Django 4.1.2 on 2022-10-26 10:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0013_alter_dealwithclient_document_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dealwithclient',
            options={'ordering': ['id'], 'verbose_name': 'Угоди', 'verbose_name_plural': 'Угоди'},
        ),
        migrations.AlterField(
            model_name='dealwithclient',
            name='document',
            field=models.ImageField(blank=True, null=True, upload_to='photos/<django.db.models.query_utils.DeferredAttribute object at 0x00000239AE83FF40>/'),
        ),
        migrations.AlterField(
            model_name='dealwithclient',
            name='unique',
            field=models.UUIDField(auto_created=uuid.UUID('d125e1e4-551a-11ed-a583-2c4d54929b0f'), default=uuid.UUID('d125e1e3-551a-11ed-a5ec-2c4d54929b0f')),
        ),
    ]