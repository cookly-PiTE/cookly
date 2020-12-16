from django.urls import path
import uuid
from . import views
from .views import RecipeListView, RecipeDetailView, SearchResultsListView, RecipeCreateView

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipe_list"),
    path("<uuid:pk>", RecipeDetailView.as_view(), name="recipe_detail"),
    path("add/", RecipeCreateView.as_view(), name="recipe_add"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
