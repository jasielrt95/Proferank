# Generated by Django 4.1.6 on 2023-02-05 07:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("professors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.MinLengthValidator(8),
                            django.core.validators.MaxLengthValidator(100),
                        ],
                    ),
                ),
                (
                    "codification",
                    models.CharField(
                        max_length=8,
                        validators=[
                            django.core.validators.MinLengthValidator(8),
                            django.core.validators.MaxLengthValidator(8),
                        ],
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "professor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="professors.professor",
                    ),
                ),
            ],
        ),
    ]
