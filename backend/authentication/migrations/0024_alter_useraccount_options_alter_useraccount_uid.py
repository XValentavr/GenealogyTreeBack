# Generated by Django 4.1.2 on 2022-10-26 10:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0023_alter_useraccount_uid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraccount',
            options={'ordering': ['id'], 'verbose_name': 'Користувачі', 'verbose_name_plural': 'Користувачі'},
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('d1240d1d-551a-11ed-86d7-2c4d54929b0f')),
        ),
    ]
