from djongo import models
from enumchoicefield import ChoiceEnum, EnumChoiceField

# Create your models here.


class DifficultyTypes(ChoiceEnum):
    pass


class MealCost(ChoiceEnum):
    pass


class Ingredient(models.Model):
    name = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Recipe(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=300, null=False, default=None)
    description = models.TextField(null=False, default=None)
    instructions = models.TextField(null=False, default=None)
    ingredients = models.ArrayField(
        model_container=Ingredient,
    )
    course_type = models.CharField(max_length=150, null=False, default=None)
    difficulty = models.CharField(max_length=100)
    cooking_method = models.CharField(max_length=150, null=False, default=None)
    cost = models.CharField(max_length=100)
    is_vegetarian = models.BooleanField(null=True)
    n_reviews = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0)

    objects = models.DjongoManager()

    def __str__(self):
        return self.name
