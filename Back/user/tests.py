from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User


class UserSignupApiTest(APITestCase):
    def setUp(self):
        self.signup_url = "/user/signup/"

        self.valid_user_data = {
            "username": "400243068",
            "password": "Hogo@1382",
            "email": "testuser@example.com",
            "type": "student",
        }
        
        self.invalid_user_data = {
            "username": "",
            "password": "testpassword123",
            "email": "testuser@example.com",
            "type": "student",
        }

    def test_user_signup_success(self):
        response = self.client.post(self.signup_url, data=self.valid_user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["msg"], "ok")
        self.assertIn("access_token", response.data["data"])
        self.assertIn("refresh_token", response.data["data"])
        self.assertEqual(response.data["data"]["user"]["username"], self.valid_user_data["username"])
        self.assertEqual(response.data["data"]["user"]["email"], self.valid_user_data["email"])
        
        self.assertTrue(User.objects.filter(username=self.valid_user_data["username"]).exists())
        
        created_user = User.objects.get(username=self.valid_user_data["username"])
        self.assertTrue(created_user.entry_year, 400)

    def test_user_signup_failure(self):
        response = self.client.post(self.signup_url, data=self.invalid_user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "error")
        self.assertIn("username", response.data["data"])
        self.assertIn("password", response.data["data"])        
        self.assertFalse(User.objects.filter(email=self.invalid_user_data["email"]).exists())