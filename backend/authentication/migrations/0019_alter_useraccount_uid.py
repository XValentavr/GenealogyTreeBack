# Generated by Django 4.1.2 on 2022-10-25 12:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0018_alter_useraccount_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('46eedb6b-545d-11ed-9d77-2c4d54929b0f')),
        ),
    ]