# Generated by Django 4.1.2 on 2022-11-01 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marble', '0010_alter_marble_image_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marble',
            name='image_size',
        ),
    ]
