# Generated by Django 4.1.2 on 2022-11-01 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marble', '0009_marble_image_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marble',
            name='image_size',
            field=models.CharField(max_length=200),
        ),
    ]
