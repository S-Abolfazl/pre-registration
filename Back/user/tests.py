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
        

class UserLoginApiTest(APITestCase):
    def setUp(self):
        self.login_url = "/user/login/"

        self.test_user = User.objects.create_user(
            username="400243068",
            password="Hogo@1382",
            email="testuser@example.com",
            type="student",
            entry_year=400
        )

        self.valid_login_data = {
            "username": "400243068",
            "password": "Hogo@1382"
        }

        self.invalid_login_data = {
            "username": "400243068",
            "password": "wrongpassword"
        }

    def test_user_login_success(self):
        response = self.client.post(self.login_url, data=self.valid_login_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "ok")
        self.assertIn("access_token", response.data["data"])
        self.assertIn("refresh_token", response.data["data"])
        self.assertEqual(response.data["data"]["user"]["username"], self.valid_login_data["username"])

    def test_user_login_failure_invalid_password(self):
        response = self.client.post(self.login_url, data=self.invalid_login_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["msg"], "error")
        self.assertEqual(response.data["data"], "Invalid username or password")

    def test_user_login_failure_missing_fields(self):
        response = self.client.post(self.login_url, data={}, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["msg"], "error")
        self.assertEqual(response.data["data"], "Invalid username or password")
        

class UserListApiTest(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin",
            password="adminpassword",
            email="admin@example.com",
            type="admin",
            is_staff=True
        )
        self.student_user = User.objects.create_user(
            username="student",
            password="studentpassword",
            email="student@example.com",
            type="student",
            entry_year=400
        )
        self.list_url = "/user/list/"
        self.detail_url = f"/user/list/{self.student_user.id}"
        
        self.client.force_authenticate(user=self.admin_user)

    def test_admin_can_view_all_users(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_admin_can_view_user_by_id(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], str(self.student_user.id))
        self.assertEqual(response.data["username"], self.student_user.username)
        self.assertEqual(response.data["email"], self.student_user.email)

    def test_user_not_found(self):
        response = self.client.get("/user/list/invalid-id")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "error")

    def test_non_admin_cannot_access(self):
        self.client.logout()
        self.client.force_authenticate(user=self.student_user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)