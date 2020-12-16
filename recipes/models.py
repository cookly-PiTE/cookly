from djongo import models
from enumchoicefield import ChoiceEnum, EnumChoiceField
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid


# Create your models here.


class Ingredient(models.Model):
    name = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300, null=False, default=None)
    description = models.TextField(null=False, default=None)
    instructions = models.TextField(null=False, default=None)
    ingredients = models.ArrayField(
        model_container=Ingredient,
    )
    image_url = models.URLField(default=None)
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

    def get_absolute_url(self):
        return reverse("recipe_detail", args=[self.id])


class Review(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review