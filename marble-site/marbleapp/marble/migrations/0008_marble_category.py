# Generated by Django 4.1.2 on 2022-10-28 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marble', '0007_alter_marble_description_alter_marble_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='marble',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='marble.category'),
        ),
    ]
