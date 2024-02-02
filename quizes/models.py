from django.db import models
from django.db import models
from category.models import Category
from difficulty.models import Difficulty

# Create your models here.


class Quiz(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True
    )

    topic = models.CharField(max_length=200)
    number_of_Questions = models.IntegerField()
    marks_per_right_answer = models.FloatField(blank=True, null=True)
    deduct_marks_per_wrong_answer = models.FloatField(blank=True, null=True)
    time = models.IntegerField(help_text="duration in minute")
    required_to_pass = models.IntegerField(help_text="Percent marks to need pass")
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)

    def __str__(self):
        return f"Category -> {self.category} ||Topic -> {self.topic}"

    def get_questions(self):
        return self.question_set.all()[: self.number_of_Questions]

    class Meta:
        verbose_name_plural = "Quizes"
