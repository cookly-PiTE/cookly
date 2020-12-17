from .models import Recipe, Review
from django.urls import reverse
from django.test import Client, TestCase
from django.contrib.auth import get_user_model


class RecipeTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com'
        )

        self.recipe = Recipe.objects.create(
            name="Cake",
            description="Cake test recipe",
            ingredients=[{"name": "1/2 apple"}, {"name": "1 kg of flour"}],
            course_type="breakfast",
            difficulty="easy",
            cooking_method="baking",
            cost="inexpensive",
        )

        self.review = Review.objects.create(
            recipe = self.recipe,
            author = self.user,
            review = 'Test review',
        )

    def test_recipe_listing(self):
        self.assertEqual(f"{self.recipe.name}", "Cake")
        self.assertEqual(f"{self.recipe.description}", "Cake test recipe")
        self.assertEqual(f"{self.recipe.cost}", "inexpensive")

    def test_recipe_list_view(self):
        response = self.client.get(reverse("recipe_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cake")
        self.assertTemplateUsed(response, "recipes/recipe_list.html")

    def test_recipe_detail_view(self):
        response = self.client.get(self.recipe.get_absolute_url())
        no_response = self.client.get("/recipes/123/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Cake")
        self.assertContains(response, 'Test review')
        self.assertTemplateUsed(response, "recipes/recipe_detail.html")
