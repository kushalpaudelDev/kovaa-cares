from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class SmokeTests(TestCase):
    def setUp(self):
        self.client = Client()
        user_model = get_user_model()
        
        self.user = user_model.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='pass1234'
        )
        self.admin = user_model.objects.create_superuser(
            username='admin', 
            email='admin@example.com', 
            password='adminpass'
        )

    def test_home_and_register_pages(self):
        self.assertEqual(self.client.get(reverse('home')).status_code, 200)
        self.assertEqual(self.client.get(reverse('register')).status_code, 200)

    def test_dashboard_requires_login_and_loads(self):
        response = self.client.get(reverse('dashboard'))
        self.assertIn(response.status_code, (301, 302))

        self.assertTrue(self.client.login(username='testuser', password='pass1234'))
        self.assertEqual(self.client.get(reverse('dashboard')).status_code, 200)

    def test_admin_index_accessible_by_superuser(self):
        self.client.force_login(self.admin)
        self.assertEqual(self.client.get(reverse('admin:index')).status_code, 200)
