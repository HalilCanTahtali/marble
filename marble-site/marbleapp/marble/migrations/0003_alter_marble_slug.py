# Generated by Django 4.1.2 on 2022-10-28 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marble', '0002_marble_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marble',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]