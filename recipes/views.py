from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Recipe


class RecipeList(ListView):
    model = Recipe
    paginate_by = 40
    template_name = "recipes/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.all()
        return context