# Generated by Django 4.2.7 on 2024-02-03 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('difficulty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='difficulty',
            name='slug',
            field=models.SlugField(blank=True, max_length=225, null=True, unique=True),
        ),
    ]
