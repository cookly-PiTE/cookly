from django.urls import path

from . import views

urlpatterns = [
    path('/recipies', views.index, name='index'),
]