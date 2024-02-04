from django.db import models
from quizes.models import Quiz
from django.contrib.auth.models import User


# Create your models here.
class Quiz_Taken(models.Model):
    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    score = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.quiz_name.topic} quiz is taken by {self.user}"
