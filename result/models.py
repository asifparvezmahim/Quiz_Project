from django.db import models
from quizes.models import Quiz
from django.contrib.auth.models import User


# Create your models here.
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    exam_name = models.CharField(max_length=500, blank=True, null=True)
    total_questions = models.CharField(max_length=500, blank=True, null=True)
    percent = models.CharField(max_length=500, blank=True, null=True)
    fullMarks = models.CharField(max_length=500, blank=True, null=True)
    total_quizes = models.CharField(max_length=100, blank=True, null=True)
    completed_quizes = models.CharField(max_length=100, blank=True, null=True)
    percent_of_attempts = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.pk)
