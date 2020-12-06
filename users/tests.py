from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model


class RegisterPageTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testuser123'
        self.email = 'testuser123@gmail.com'
    

    def test_register_page_status_code(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
    
    def test_register_page_template_used(self):
        response = self.client.get(reverse("register"))
        self.assertTemplateUsed(response, "users/register.html")

    def test_registration_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)

        all_users = get_user_model().objects.all()


        self.assertEqual(all_users.count(), 1)
        self.assertEqual(all_users[0].email, self.email)
        self.assertEqual(all_users[0].username, self.username)