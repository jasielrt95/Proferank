# Generated by Django 4.1.4 on 2022-12-31 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0002_professor_created_at_professor_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='professor',
            name='total_reviews',
            field=models.IntegerField(default=0),
        ),
    ]
