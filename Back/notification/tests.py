from rest_framework.test import APITestCase
from rest_framework import status

from user.models import User
from .models import Notification

class NitificationGetApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user",
            password="password",
            email="h@g.com",
            type="student"
        )
        
        self.notification = Notification.objects.create(
            title="title",
            content="content"
        )
        
        self.client.force_authenticate(user=self.user)
        
    def test_get_notification_success(self):
        response = self.client.get("/notification/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "ok")
        self.assertIn("data", response.data)
        self.assertIsInstance(response.data["data"], list)
        self.assertEqual(self.notification.__str__(), response.data["data"][0]["title"])