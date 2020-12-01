from django.urls import path

from . import views
from .views import RecipeList

urlpatterns = [
    path('', RecipeList.as_view()),
]