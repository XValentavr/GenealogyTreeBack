# Generated by Django 4.1.2 on 2022-10-27 21:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0033_alter_useraccount_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('9031f42e-563c-11ed-b7e7-3ca0670b2ec7')),
        ),
    ]