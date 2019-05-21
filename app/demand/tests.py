from django.contrib.auth import get_user_model
from app import settings
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from demand.models import Demand


class ApiTestCase(APITestCase):

    def setUp(self):
        user = get_user_model()
        self.user = user.objects.create_user(name='andrewfortest',
                                             email='andrew@dstest.com',
                                             password='12345')
        self.information = {'title': 'New_test',
                            'from_user': self.user.id,
                            'content': 'test_content',
                            'to_creator': self.user.id + 1}

    def authorize(self, user, **additional_headers):
        token = AccessToken.for_user(user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'{settings.SIMPLE_JWT["AUTH_HEADER_TYPES"][0]} {token}',
            **additional_headers)

    def create_and_authorize(self, **additional_headers):
        user = self.user()
        self.authorize(user, **additional_headers)
        return user

    """POST tests"""

    def test_post_demand_unauthorized(self):
        resp = self.client.post('/api/demands/', data=self.information)
        self.assertEqual(resp.status_code, 401)

    def test_post_demand_bad_request(self):
        self.authorize(self.user)
        resp = self.client.post('/api/demands/', data=self.information)
        self.assertEqual(resp.status_code, 400)

    def test_post_demand(self):
        self.authorize(self.user)
        information = {'title': 'New_test',
                       'from_user': self.user.id,
                       'content': 'test_content',
                       'to_creator': self.user.id}

        resp = self.client.post('/api/demands/', data=information)
        self.assertEqual(resp.status_code, 201)

    """GET tests"""

    def test_get_all_demands_unauthorized(self):
        resp = self.client.get('/api/demands/')
        self.assertEqual(resp.status_code, 401)

    def test_get_all_demands_fail(self):
        self.authorize(self.user)
        resp = self.client.get('/api/demands_/')
        self.assertEqual(resp.status_code, 404)

    def test_get_all_demands(self):
        self.authorize(self.user)
        resp = self.client.get('/api/demands/')
        self.assertEqual(resp.status_code, 200)

    def test_get_one_demand(self):
        self.authorize(self.user)
        new_demand = Demand(title='New_test',
                            from_user=self.user,
                            content='test_content',
                            to_creator=self.user)
        new_demand.save()
        resp = self.client.get(f'/api/demands/{new_demand.id}/')
        self.assertEqual(resp.status_code, 200)

    def test_get_one_demand_404(self):
        self.authorize(self.user)
        new_demand = Demand(title='New_test',
                            from_user=self.user,
                            content='test_content',
                            to_creator=self.user)
        new_demand.save()
        resp = self.client.get(f'/api/demands/{new_demand.id + 1}/')
        self.assertEqual(resp.status_code, 404)

