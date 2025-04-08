# Тесты с использованием базового unittest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UrlsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass123")

    def test_home_url_accessible(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_kras_url_accessible(self):
        response = self.client.get(reverse('kras'))
        self.assertEqual(response.status_code, 200)

    def test_stolbiki_url_accessible(self):
        response = self.client.get(reverse('stolb'))
        self.assertEqual(response.status_code, 200)

    def test_add_item_redirects_for_anonymous(self):
        response = self.client.get(reverse('add_item'))
        self.assertEqual(response.status_code, 302)  # редирект на логин

    def test_add_item_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse('add_item'))
        self.assertEqual(response.status_code, 200)

class RegistrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_register_page_loads(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_register_form_valid(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'VeryStrongPass123',
            'password2': 'VeryStrongPass123'
        })
        self.assertEqual(response.status_code, 302)  # редирект после регистрации
        self.assertTrue(User.objects.filter(username='newuser').exists())
