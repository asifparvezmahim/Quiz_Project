# Generated by Django 4.2.7 on 2024-02-02 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_result_total_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='correct_ans',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='not_ans',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='wrong_ans',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
