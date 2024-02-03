from django.contrib import admin
from .models import Difficulty


# Register your models here.
class DifficultyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]


admin.site.register(Difficulty, DifficultyAdmin)
