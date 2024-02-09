from django.db import models
from django.contrib.auth.models import User
from quizes.models import Quiz

# Create your models here.
rating = {
    "*": "*",
    "**": "**",
    "***": "***",
    "****": "****",
    "*****": "*****",
}


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"User -> {self.user} --- {self.quiz}"
