from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=225, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
