from app.user_for_tests import APITestUser
from lesson.models import Lessons, Like


class ApiTestCase(APITestUser):

    def setUp(self):
        self.user = self.create_and_authorize(email='tessast@gmail.com', password='testpass132', name='test')
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
        information = {'tittle': 'New_test', 'author': self.user.email}
        resp = self.client.post('/api/lessons/', data=information)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data['author'], self.user.email)

    def test_lesson_creation_fail_bad_request(self):
        information = {'tittle': 'New_test', 'fake_author': self.user.id}
        resp = self.client.post('/api/lessons/', data=information)
        self.assertEqual(resp.status_code, 400)

    def test_lesson_creation_fail_404(self):
        information = {'tittle': 'New_test', 'author': self.user.id}
        resp = self.client.post('/api/lessons_test/', data=information)
        self.assertEqual(resp.status_code, 404)

    def test_lesson_not_create_with_anonymous_user(self):
        self.logout()
        information = {'tittle': 'New_test', 'author': self.user.id}
        resp = self.client.post("/api/lessons/", data=information)
        self.assertEqual(resp.status_code, 401)

    def test_get_likes(self):
        resp = self.client.get(f'/api/lessons/{self.new_lesson.id}/likes/')
        self.assertEqual(resp.status_code, 200)

    def test_get_likes_fail(self):
        resp = self.client.get(f'/api/lessons/{self.new_lesson.id + 22054}/likes/')
        self.assertEqual(resp.status_code, 404)

    def test_get_likes_fail_two(self):
        resp = self.client.get(f'/api/lessons/{self.new_lesson.id}/likes_/')
        self.assertEqual(resp.status_code, 404)

    def test_like_create_successful(self):
        resp = self.client.post(f'/api/lessons/{self.new_lesson.id}/likes/toggle/')
        self.assertEqual(resp.status_code, 201)
        like_exists = Like.objects.filter(lesson=self.new_lesson,
                                          user=self.user).exists()
        self.assertTrue(like_exists)

    def test_error_anon_user(self):
        self.logout()
        resp = self.client.post(f'/api/lessons/{self.new_lesson.id}/likes/toggle/')
        self.assertEqual(resp.status_code, 401)

    def test_get_all_likes_from_lesson(self):
        self.client.post(f'/api/lessons/{self.new_lesson.id}/likes/toggle/')
        resp = self.client.get(f'/api/lessons/{self.new_lesson.id}/likes/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['count'], 1)

    def test_get_error_if_anon_user_get_likes(self):
        self.logout()
        resp = self.client.get(f'/api/lessons/{self.new_lesson.id}/likes/')
        self.assertEqual(resp.status_code, 401)
