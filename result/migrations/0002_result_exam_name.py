# Generated by Django 4.2.7 on 2024-02-02 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='exam_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
