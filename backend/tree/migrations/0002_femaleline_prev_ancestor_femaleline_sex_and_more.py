# Generated by Django 4.1.2 on 2022-12-11 12:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0001_initial"),
        ("tree", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="femaleline",
            name="prev_ancestor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="tree.femaleline",
            ),
        ),
        migrations.AddField(
            model_name="femaleline",
            name="sex",
            field=models.CharField(default="Ж", max_length=10),
        ),
        migrations.AddField(
            model_name="mainrootuserspouse",
            name="sex",
            field=models.CharField(default="М", max_length=10),
        ),
        migrations.AddField(
            model_name="mainrootuserwife",
            name="sex",
            field=models.CharField(default="М", max_length=10),
        ),
        migrations.AddField(
            model_name="maleline",
            name="prev_ancestor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="tree.maleline",
            ),
        ),
        migrations.AddField(
            model_name="maleline",
            name="sex",
            field=models.CharField(default="М", max_length=10),
        ),
        migrations.AlterField(
            model_name="femaleline",
            name="document",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="documents.documents",
            ),
        ),
        migrations.AlterField(
            model_name="femaleline",
            name="unique_female",
            field=models.UUIDField(
                default=uuid.UUID("cbb5068d-794e-11ed-a9b7-2c3b706d7921")
            ),
        ),
        migrations.AlterField(
            model_name="mainrootuser",
            name="unique_root",
            field=models.UUIDField(
                default=uuid.UUID("cbb4defe-794e-11ed-a3ff-2c3b706d7921")
            ),
        ),
        migrations.AlterField(
            model_name="mainrootuserspouse",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("cbb4df00-794e-11ed-a4b0-2c3b706d7921"), unique=True
            ),
        ),
        migrations.AlterField(
            model_name="mainrootuserwife",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("cbb4deff-794e-11ed-a09e-2c3b706d7921"), unique=True
            ),
        ),
        migrations.AlterField(
            model_name="maleline",
            name="document",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="documents.documents",
            ),
        ),
        migrations.AlterField(
            model_name="maleline",
            name="unique_male",
            field=models.UUIDField(
                default=uuid.UUID("cbb5068e-794e-11ed-a3fc-2c3b706d7921")
            ),
        ),
        migrations.CreateModel(
            name="MaleLineChild",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255, null=True)),
                ("surname", models.CharField(max_length=255, null=True)),
                ("last_name", models.CharField(max_length=255, null=True)),
                ("mother_surname", models.CharField(max_length=255, null=True)),
                ("date_of_birth", models.DateField(default=None, null=True)),
                ("place_of_birth", models.CharField(max_length=255, null=True)),
                ("date_of_marry", models.DateField(default=None, null=True)),
                ("date_of_death", models.DateField(default=None, null=True)),
                ("is_published", models.BooleanField(default=False)),
                (
                    "unique_male_child",
                    models.UUIDField(
                        default=uuid.UUID("cbb52d9e-794e-11ed-a93a-2c3b706d7921")
                    ),
                ),
                ("sex", models.CharField(default="Ж", max_length=10)),
                (
                    "document",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="documents.documents",
                    ),
                ),
                (
                    "next_ancestor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="tree.malelinechild",
                    ),
                ),
                (
                    "root",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tree.mainrootuser",
                    ),
                ),
            ],
            options={
                "verbose_name": "Інформація про дітей по чоловічій лінії",
                "verbose_name_plural": "Інформація про дітей по чоловічій лінії",
            },
        ),
        migrations.CreateModel(
            name="FemaleLineChild",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255, null=True)),
                ("surname", models.CharField(max_length=255, null=True)),
                ("last_name", models.CharField(max_length=255, null=True)),
                ("mother_surname", models.CharField(max_length=255, null=True)),
                ("date_of_birth", models.DateField(default=None, null=True)),
                ("place_of_birth", models.CharField(max_length=255, null=True)),
                ("date_of_marry", models.DateField(default=None, null=True)),
                ("date_of_death", models.DateField(default=None, null=True)),
                ("is_published", models.BooleanField(default=False)),
                (
                    "unique_female",
                    models.UUIDField(
                        default=uuid.UUID("cbb52d9d-794e-11ed-bd52-2c3b706d7921")
                    ),
                ),
                ("sex", models.CharField(default="М", max_length=10)),
                (
                    "document",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="documents.documents",
                    ),
                ),
                (
                    "next_ancestor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="tree.femalelinechild",
                    ),
                ),
                (
                    "root",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tree.mainrootuser",
                    ),
                ),
            ],
            options={
                "verbose_name": "Інформація по чоловічій лінії",
                "verbose_name_plural": "Інформація по чоловічій лінії",
            },
        ),
    ]
