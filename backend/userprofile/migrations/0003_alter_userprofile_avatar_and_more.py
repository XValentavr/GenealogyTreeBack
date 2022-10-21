# Generated by Django 4.1.2 on 2022-10-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_alter_userprofile_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lastname',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telegram',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='whatsapp',
            field=models.URLField(default=None, null=True),
        ),
    ]
