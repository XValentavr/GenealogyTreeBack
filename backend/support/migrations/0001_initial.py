# Generated by Django 4.1.2 on 2022-10-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('context', models.TextField()),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Технічна підтримка',
                'verbose_name_plural': 'Технічна підтримка',
                'ordering': ['id'],
            },
        ),
    ]
