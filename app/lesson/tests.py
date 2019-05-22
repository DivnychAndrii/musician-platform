from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from lesson.models import Lessons



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

    def test_lesson_creation(self):
        information = {'tittle': 'New_test', 'author': self.user.id}
        resp = self.client.post('/api/lessons/', data=information)
        self.assertEqual(resp.status_code, 201)

    def test_lesson_creation_fail_bad_request(self):
        information = {'tittle': 'New_test', 'fake_author': self.user.id}
        resp = self.client.post('/api/lessons/', data=information)
        self.assertEqual(resp.status_code, 400)

    def test_lesson_creation_fail_404(self):
        information = {'tittle': 'New_test', 'author': self.user.id}
        resp = self.client.post('/api/lessons_test/', data=information)
        self.assertEqual(resp.status_code, 404)

    def test_get_likes(self):
        resp = self.client.get(f'/api/lessons/{self.new_lesson.id}/likes/')
        self.assertEqual(resp.status_code, 200)

    def test_get_likes_fail(self):
        resp = self.client.get(f'/api/lessons/{self.new_lesson.id + 22054}/likes/')
        self.assertEqual(resp.status_code, 404)

    def test_get_likes_fail_two(self):
        resp = self.client.get(f'/api/lessons/{self.new_lesson.id}/likes_/')
        self.assertEqual(resp.status_code, 404)

    # def test_like_lesson(self):
    #          resp = self.client.post('/api/lessons/', data=information)
    #          self.assertEqual(resp.status_code, 201)
    #          like_exists = Like.objects.filter(lesson=self.lesson,
    #                                            liker=self.user).exists()
    #          self.assertTrue(like_exists)

