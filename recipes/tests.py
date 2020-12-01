import unittest
from django.test import Client
from .models import Recipe


class TestUrls(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_recipes_url(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)


class RecipeTestCase(unittest.TestCase):
    def setUp(self):
        Recipe.objects.create(
            name="Cake",
            description="This is a test recipe",
            ingredients=[{"name": "1/2 apple"}, {"name": "1 kg of flour"}],
            course_type="breakfast",
            difficulty="easy",
            cooking_method="baking",
            cost="inexpensive",
        )
        Recipe.objects.create(
            name="Pie",
            description="Test 2",
            ingredients=[{"name": "3 eggs"}, {"name": "2 bananas"}],
            course_type="breakfast",
            difficulty="easy",
            cooking_method="baking",
            cost="expensive",
        )

    def test_animals_can_speak(self):
        cake = Recipe.objects.get(name="Cake")
        pie = Recipe.objects.get(name="Pie")
        self.assertEqual(str(cake), "Cake")
        self.assertEqual(str(pie), "Pie")
