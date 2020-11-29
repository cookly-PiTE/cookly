from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField

# Create your models here.


class DifficultyTypes(ChoiceEnum):
    pass


class MealCost(ChoiceEnum):
    pass


class Recipe(models.Model):
    name = models.CharField(max_length=300, null=False, default=None)
    description = models.TextField(null=False, default=None)
    instruction = models.TextField(null=False, default=None)
    course_type = models.CharField(max_length=150, null=False, default=None)
    difficulty = models.CharField(max_length=100)
    cooking_method = models.CharField(max_length=150, null=False, default=None)
    cost = models.CharField(max_length=100)
    is_vegetarian = models.BooleanField()


class Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )
    name = models.TextField()
