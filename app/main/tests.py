from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):

        email = 'test@test.com'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_email_fail(self):
        email = '123@email.com'
        password = '1234'
        user = get_user_model().objects.create_user(
            email='test123@email.com',
            password='12345'
        )
        self.assertNotEqual(user.email, email)
        self.assertFalse(user.check_password(password))

    def test_new_user_email_normalize(self):

        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email, "1234")

        self.assertEqual(user.email, email.lower())


class TestAuthentication(APITestCase):

    def setUp(self):
        self.email, self.password = "testtest@test.com", "12345"
        self.user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password
        )

    def test_auth(self):
        data = {
            "email": self.email,
            "password": self.password
        }
        resp = self.client.post(reverse('auth'), data=data)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('access', resp.data)
        self.assertIn('refresh', resp.data)

    def test_auth_refresh(self):
        data = {
            "email": self.email,
            "password": self.password
        }
        resp = self.client.post(reverse('auth'), data=data)
        resp = self.client.post(reverse('auth-refresh'),
                                data={'refresh': resp.data["refresh"]})
        self.assertEqual(resp.status_code, 200)
