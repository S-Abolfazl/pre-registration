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


class RegistrationFormListViewTest(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(
            username="adminuser",
            password="Admin@1234",
            email="admin@example.com",
            type="admin",
            is_staff=True,
            is_superuser=True
        )
        self.non_admin_user = User.objects.create_user(
            username="regularuser",
            password="User@1234",
            email="user@example.com",
            type="student"
        )
        self.registration_form = RegistrationForm.objects.create(
            student_id=self.non_admin_user
        )
        
        self.client.force_authenticate(user=self.admin_user)

    def test_get_all_registration_forms_success(self):
        response = self.client.get("/registration-form/list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "ok")
        self.assertIn("data", response.data)
        self.assertEqual(len(response.data["data"]), 1)

    def test_get_single_registration_form_success(self):
        response = self.client.get(f"/registration-form/list/{self.registration_form.form_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "ok")
        self.assertIn("data", response.data)
        self.assertEqual(response.data["data"]["form_id"], str(self.registration_form.form_id))

    def test_get_single_registration_form_not_found(self):
        response = self.client.get("/registration-form/list/invalid-form-id/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_registration_forms_unauthorized(self):
        self.client.logout()
        response = self.client.get("/registration-form/list/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        
class RegistrationFormUpdateViewTest(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(
            username="adminuser",
            password="Admin@1234",
            email="admin@example.com",
            is_staff=True
        )
        self.non_admin_user = User.objects.create_user(
            username="regularuser",
            password="User@1234",
            email="user@example.com"
        )
        self.registration_form = RegistrationForm.objects.create(
            student_id=self.non_admin_user
        )
        self.client.force_authenticate(user=self.admin_user)

    def test_update_registration_form_success(self):
        updated_data = {
            "student_id": self.non_admin_user.id
        }
        response = self.client.put(
            f"/registration-form/update/{self.registration_form.form_id}/",
            data=updated_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "ok")
        self.assertEqual(response.data["data"]["student_id"], self.non_admin_user.id)

    def test_update_registration_form_not_found(self):
        updated_data = {
            "student_id": self.non_admin_user.id
        }
        response = self.client.put("/registration-form/update/invalid-form-id/", data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_registration_form_invalid_data(self):
        invalid_data = {
            "student_id": "invalid-student-id"
        }
        response = self.client.put(
            f"/registration-form/{self.registration_form.form_id}/",
            data=invalid_data
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_registration_form_unauthorized(self):
        self.client.logout()
        updated_data = {
            "student_id": self.non_admin_user.id
        }
        response = self.client.put(
            f"/registration-form/update/{self.registration_form.form_id}/",
            data=updated_data
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        
