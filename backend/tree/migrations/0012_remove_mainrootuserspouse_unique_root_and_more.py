# Generated by Django 4.1.2 on 2022-10-27 21:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0011_remove_mainrootuserwife_unique_root_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainrootuserspouse',
            name='unique_root',
        ),
        migrations.AddField(
            model_name='mainrootuserspouse',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('903576db-563c-11ed-8e40-3ca0670b2ec7')),
        ),
        migrations.AlterField(
            model_name='femaleline',
            name='document',
            field=models.ImageField(blank=True, null=True, upload_to='tree/<django.db.models.query_utils.DeferredAttribute object at 0x00000132DE85F550>/female'),
        ),
        migrations.AlterField(
            model_name='femaleline',
            name='unique_female',
            field=models.UUIDField(default=uuid.UUID('90359daa-563c-11ed-aba8-3ca0670b2ec7')),
        ),
        migrations.AlterField(
            model_name='mainrootuser',
            name='unique_root',
            field=models.UUIDField(default=uuid.UUID('90352875-563c-11ed-9f34-3ca0670b2ec7')),
        ),
        migrations.AlterField(
            model_name='mainrootuserwife',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('90354f9c-563c-11ed-a33e-3ca0670b2ec7')),
        ),
        migrations.AlterField(
            model_name='maleline',
            name='document',
            field=models.ImageField(blank=True, null=True, upload_to='tree/<django.db.models.query_utils.DeferredAttribute object at 0x00000132DE85F550>/male'),
        ),
        migrations.AlterField(
            model_name='maleline',
            name='unique_male',
            field=models.UUIDField(default=uuid.UUID('9035c4b0-563c-11ed-8432-3ca0670b2ec7')),
        ),
    ]
