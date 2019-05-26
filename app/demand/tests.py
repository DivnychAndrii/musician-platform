from app.user_for_tests import APITestUser
from demand.models import Demand


class ApiTestCase(APITestUser):

    def setUp(self):
        self.user = self.create_and_authorize(email='tessast@gmail.com', password='testpass132', name='test')
        self.information = {'title': 'New_test',
                            'from_user': self.user.id,
                            'content': 'test_content',
                            'to_creator': self.user.id + 1}

    """POST tests"""

    def test_post_demand_unauthorized(self):
        self.logout()
        resp = self.client.post('/api/demands/', data=self.information)
        self.assertEqual(resp.status_code, 401)

    def test_post_demand_bad_request(self):
        resp = self.client.post('/api/demands/', data=self.information)
        self.assertEqual(resp.status_code, 400)

    def test_post_demand(self):
        information = {'title': 'New_test',
                       'from_user': self.user.email,
                       'content': 'test_content',
                       'to_creator': self.user.email}
        resp = self.client.post('/api/demands/', data=information)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data['from_user'], self.user.email)

    """GET tests"""

    def test_get_all_demands_unauthorized(self):
        self.logout()
        resp = self.client.get('/api/demands/')
        self.assertEqual(resp.status_code, 401)

    def test_get_all_demands_fail(self):
        resp = self.client.get('/api/demands_/')
        self.assertEqual(resp.status_code, 404)

    def test_get_all_demands(self):
        resp = self.client.get('/api/demands/')
        self.assertEqual(resp.status_code, 200)

    def test_get_one_demand(self):
        new_demand = Demand(title='New_test',
                            from_user=self.user,
                            content='test_content',
                            to_creator=self.user)
        new_demand.save()
        resp = self.client.get(f'/api/demands/{new_demand.id}/')
        self.assertEqual(resp.status_code, 200)

    def test_get_one_demand_404(self):
        new_demand = Demand(title='New_test',
                            from_user=self.user,
                            content='test_content',
                            to_creator=self.user)
        new_demand.save()
        resp = self.client.get(f'/api/demands/{new_demand.id + 1}/')
        self.assertEqual(resp.status_code, 404)
