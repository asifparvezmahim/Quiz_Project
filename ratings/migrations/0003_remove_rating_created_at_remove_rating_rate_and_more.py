# Generated by Django 4.2.7 on 2024-02-09 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_rename_ratings_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='rate',
        ),
        migrations.AddField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
