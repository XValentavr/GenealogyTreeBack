# Generated by Django 4.1.2 on 2022-10-26 16:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0024_alter_useraccount_options_alter_useraccount_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('2d4c8104-5549-11ed-aaca-2c4d54929b0f')),
        ),
    ]