import unittest
from django.test import Client


class TestUrls(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_recipes_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
