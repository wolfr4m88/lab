import unittest
import uuid
import logging_service
import facade_service
import message_service
from flask import json

class FacadeServiceTest(unittest.TestCase):
    def setUp(self):
        self.app = facade_service.app.test_client()
        self.app.testing = True

    def test_post_data(self):
        data = {"msg": "Hello World"}
        response = self.app.post('/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Message with id", response.data.decode())

    def test_get_data(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
