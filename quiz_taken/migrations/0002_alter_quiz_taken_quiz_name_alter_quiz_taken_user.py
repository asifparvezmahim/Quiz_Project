# Generated by Django 4.2.7 on 2024-02-04 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0003_alter_quiz_deduct_marks_per_wrong_answer_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz_taken', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz_taken',
            name='quiz_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quizes.quiz'),
        ),
        migrations.AlterField(
            model_name='quiz_taken',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
