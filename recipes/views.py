from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    paginate_by = 10
    context_object_name = "recipe_list"
    template_name = "recipes/recipe_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"


class SearchResultsListView(ListView):
    model = Recipe
    paginate_by = 10
    strict = False
    context_object_name = "recipe_list"
    template_name = "recipes/search_results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Recipe.objects.filter(Q(name__icontains=query))
