# Generated by Django 4.1.2 on 2022-10-26 16:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0002_alter_femaleline_options_alter_mainrootuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='femaleline',
            name='document',
            field=models.ImageField(blank=True, null=True, upload_to='tree/<django.db.models.query_utils.DeferredAttribute object at 0x00000202B9B34190>/female'),
        ),
        migrations.AlterField(
            model_name='femaleline',
            name='unique_female',
            field=models.UUIDField(default=uuid.UUID('2d513bf2-5549-11ed-9453-2c4d54929b0f')),
        ),
        migrations.AlterField(
            model_name='mainrootuser',
            name='unique_root',
            field=models.UUIDField(default=uuid.UUID('2d502ac3-5549-11ed-a6e1-2c4d54929b0f')),
        ),
        migrations.AlterField(
            model_name='maleline',
            name='document',
            field=models.ImageField(blank=True, null=True, upload_to='tree/<django.db.models.query_utils.DeferredAttribute object at 0x00000202B9B34190>/male'),
        ),
        migrations.AlterField(
            model_name='maleline',
            name='unique_male',
            field=models.UUIDField(default=uuid.UUID('2d518a2d-5549-11ed-8a5f-2c4d54929b0f')),
        ),
        migrations.CreateModel(
            name='MainRootUserWife',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('surname', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('mother_surname', models.CharField(max_length=255, null=True)),
                ('date_of_birth', models.DateField(default=None, null=True)),
                ('place_of_birth', models.CharField(max_length=255, null=True)),
                ('date_of_marry', models.DateField(default=None, null=True)),
                ('is_dead', models.BooleanField(default=False)),
                ('date_of_death', models.DateField(default=None, null=True)),
                ('years', models.CharField(default=None, max_length=255, null=True)),
                ('unique_root', models.UUIDField(default=uuid.UUID('2d5051de-5549-11ed-8507-2c4d54929b0f'))),
                ('spouse', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tree.mainrootuser')),
            ],
            options={
                'verbose_name': 'Дружина',
                'verbose_name_plural': 'Дружина',
                'ordering': ['id'],
            },
        ),
    ]
