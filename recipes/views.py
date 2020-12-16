from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    paginate_by = 10
    context_object_name = "recipe_list"
    template_name = "recipes/recipe_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipes/recipe_add.html"
    fields = ['name', 'description', 'instructions', 'course_type', 'cost', 'is_vegetarian', 'cooking_method']


class SearchResultsListView(ListView):
    model = Recipe
    paginate_by = 10
    strict = False
    context_object_name = "recipe_list"
    template_name = "recipes/search_results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cost"] = self.request.GET.get("cost")
        context["name_contains"] = self.request.GET.get("name_contains")
        context["cooking_method"] = self.request.GET.get("cooking_method")
        return context

    def get_queryset(self):
        cost = self.request.GET.get("cost")
        name_contains = self.request.GET.get("name_contains")
        cooking_method = self.request.GET.get("cooking_method")
        if not cooking_method and cost:
            recipes = Recipe.objects.filter(
                Q(cost=cost) & Q(name__icontains=name_contains)
            )
        elif not cost and cooking_method:
            recipes = Recipe.objects.filter(
                Q(name__icontains=name_contains)
                & Q(cooking_method__icontains=cooking_method)
            )
        elif cost is None and cooking_method is None:
            recipes = Recipe.objects.filter(Q(name__icontains=name_contains))
        else:
            recipes = Recipe.objects.filter(
                Q(cost=cost)
                & Q(name__icontains=name_contains)
                & Q(cooking_method__icontains=cooking_method)
            )
        return recipes
