# Generated by Django 4.2.7 on 2024-02-03 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizes', '0003_alter_quiz_deduct_marks_per_wrong_answer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz_Taken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
