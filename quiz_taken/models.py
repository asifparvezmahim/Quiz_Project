from django.db import models
from quizes.models import Quiz
from django.contrib.auth.models import User


# Create your models here.
class Quiz_Taken(models.Model):
    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
