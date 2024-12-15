from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

from .models import RegistrationForm
from user.models import User

class RegistrationFormCreateViewTest(APITestCase):
    def setUp(self):
        self.student_user = User.objects.create_user(
            username="teststudent",
            password="Test@1234",
            email="student@example.com",
            type="student"
        )
        
        self.client.force_authenticate(user=self.student_user)

    def test_create_registration_form_success(self):
        response = self.client.post("/registration-form/create/")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["msg"], "ok")
        self.assertIn("data", response.data)

        registration_form = RegistrationForm.objects.filter(student_id=self.student_user).first()
        self.assertIsNotNone(registration_form)
        self.assertEqual(str(registration_form.student_id), self.student_user.username)

    def test_create_registration_form_already_exists(self):
        RegistrationForm.objects.create(student_id=self.student_user)

        response = self.client.post("/registration-form/create/")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "error")
        self.assertIn("student_id", response.data["data"])

    def test_create_registration_form_unauthenticated(self):
        self.client.logout()

        response = self.client.post("/registration-form/create/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


