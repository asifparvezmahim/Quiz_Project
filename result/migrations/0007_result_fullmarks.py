# Generated by Django 4.2.7 on 2024-02-02 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0006_rename_correct_ans_result_percent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='fullMarks',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
