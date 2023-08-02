from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import UserProfile

class UserProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserProfile.objects.create(username='testuser', email='test@example.com', bio='Test bio')

    def test_user_profile_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.bio, 'Test bio')

    def test_user_detail_view(self):
        url = reverse('user_detail', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.email)
        self.assertContains(response, self.user.bio)
