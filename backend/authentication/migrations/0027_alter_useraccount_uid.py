# Generated by Django 4.1.2 on 2022-10-27 15:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0026_alter_useraccount_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('4f5d2072-5610-11ed-b787-3ca0670b2ec7')),
        ),
    ]
