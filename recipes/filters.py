import django_filters

from .models import Recipe


class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = Recipe
        fields = {
             'cost': ['icontains'],
            'cooking_method': ['icontains'],
            'course_type': ['icontains'],
        }

