from django.contrib import admin
from .models import Recipe, Review

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review


class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]

    list_display = ('name', 'cost')


admin.site.register(Recipe, RecipeAdmin)