from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Resolution

class ResolutionModelTest(TestCase):

    def test_string_representation(self):
        resolution = Resolution(title="My Resolution")
        self.assertEqual(str(resolution), resolution.title)

class AddResolutionViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('add_resolution'))
        self.assertRedirects(response, '/login/?next=/add/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('add_resolution'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resolutions/add_resolution.html')
