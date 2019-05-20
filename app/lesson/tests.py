from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from lesson.models import Lessons
from app import settings


class ApiTestCase(APITestCase):

    def setUp(self):
        user = get_user_model()
        self.user = user.objects.create_user(name='andrewfortest',
                                             email='andrew@test.com',
                                             password='12345')
        self.new_lesson = Lessons(
                                author=self.user,
                                tittle='Test',
                                pub_date='2019-05-17')
        self.new_lesson.save()

    def test_get_all_lessons(self):
        resp = self.client.get('/api/lessons/')
        self.assertEqual(resp.status_code, 200)

    def test_get_one_lesson(self):
        resp = self.client.get(f'/api/lessons/{self.new_lesson.id}/')
        self.assertEqual(resp.status_code, 200)

    def test_get_no_lesson(self):
        resp = self.client.get(f'/api/lessons/{self.new_lesson.id +1000}/')
        self.assertEqual(resp.status_code, 404)

    # def test_lesson_creation(self):
    #     token = AccessToken.for_user(self.user)
    #     information = {'title': 'New_test'}
    #     resp = self.client.post('/api/lessons/',
    #                             HTTP_AUTHORIZATION=f'{settings.SIMPLE_JWT["AUTH_HEADER_TYPES"][0]} {token}',
    #                             data=information,)
    #     self.assertEqual(resp.status_code, 201)

    def test_get_likes(self):
        resp = self.client.get(f'/api/lessons/{self.new_lesson.id}/likes/')
        print(resp)
        self.assertEqual(resp.status_code, 200)

    def test_get_likes_fail(self):
        resp = self.client.get(f'/api/lessons/{self.new_lesson.id + 22054}/likes/')
        self.assertEqual(resp.status_code, 404)
