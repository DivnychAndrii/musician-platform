from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from . import settings


class APITestUser(APITestCase):

    def create_user(self):
        email = 'test@test.com'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(email, password)
        self.is_active = True
        user.save()
        return user

    def authorize(self, user, **additional_headers):
        token = AccessToken.for_user(user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'{settings.SIMPLE_JWT["AUTH_HEADER_TYPES"][0]} {token}',
            **additional_headers
        )

    def create_and_authorize(self, **additional_headers):
        user = self.create_user()
        self.authorize(user, **additional_headers)
        return user

    def logout(self, **additional_headers):
        self.client.credentials(**additional_headers)
