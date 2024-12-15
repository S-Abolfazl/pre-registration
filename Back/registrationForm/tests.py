from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

from .models import RegistrationForm, SelectedCourse
from user.models import User
from course.models import Course, AllCourses
from student.models import CompletedCourses
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
        
        
class RegistrationFormDeleteViewTest(APITestCase):
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

    def test_delete_registration_form_success(self):
        response = self.client.delete(f"/registration-form/delete/{self.registration_form.form_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "ok")
        self.assertIn("deleted successfully", response.data["data"])
        self.assertFalse(RegistrationForm.objects.filter(form_id=self.registration_form.form_id).exists())

    def test_delete_registration_form_not_found(self):
        response = self.client.delete("/registration-form/delete/invalid-form-id/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_registration_form_unauthorized(self):
        self.client.logout()
        response = self.client.delete(f"/registration-form/delete/{self.registration_form.form_id}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
class RegistrationFormDataApiTest(APITestCase):
    def setUp(self):
        self.student_user = User.objects.create_user(
            username="student_user", password="Test@1234", email="h@example.com", type="student"
        )
        
        self.all_course_1 = AllCourses.objects.create(
            courseName="Sample Course",
            unit=3,
            type="theory_course"
        )
        
        self.all_course_2 = AllCourses.objects.create(
            courseName="Sample Course 2",
            unit=3,
            type="theory_course"
        )
        
        
        self.course1 = Course.objects.create(
            course=self.all_course_1,
            teacherName="Dr. Smith",
            isExperimental=False,
            class_time1="شنبه",
            class_time2="دوشنبه",
            class_start_time="10:30:00",
            class_end_time="12:00:00",
            exam_date="2024-12-20",
            exam_start_time="08:00:00",
            exam_end_time="10:00:00",
            capacity=30,
            description="Sample course"
        )
        
        self.course2 = Course.objects.create(
            course=self.all_course_2,
            teacherName="Dr. Smith",
            isExperimental=False,
            class_time1="شنبه",
            class_time2="دوشنبه",
            class_start_time="09:00:00",
            class_end_time="10:30:00",
            exam_date="2024-12-20",
            exam_start_time="08:00:00",
            exam_end_time="10:00:00",
            capacity=30,
            description="Sample course 2"
        )
        
        self.completed_course = CompletedCourses.objects.create(
            student=self.student_user,
            course=self.all_course_1
        )
        
        self.selected_course = SelectedCourse.objects.create(form=RegistrationForm.objects.create(student_id=self.student_user), course=self.course2)
        self.client.force_authenticate(user=self.student_user)
        
        
    def test_get_registration_form_data_success(self):
        response = self.client.get("/registration-form/courses-data/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "ok")
        self.assertEqual(response.data["status"], status.HTTP_200_OK)
        self.assertTrue(len(response.data["data"]) == 1)
        self.assertIn("course", response.data["data"][0])
        self.assertEqual(response.data["data"][0]['c_id'], self.course2.c_id)
        self.assertEqual(response.data["data"][0]['selected'], True)

    def test_get_registration_form_data_unauthorized(self):
        self.client.logout()
        response = self.client.get("/registration-form/courses-data/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response.data)
        self.assertEqual(response.data["detail"], "Authentication credentials were not provided.")
        

class RegistrationFormConfirmApiTest(APITestCase):
    def setUp(self):
        self.student_user = User.objects.create_user(
            username="student_user", password="Test@1234", email="h@e.com", type="student"
        )
        
        self.form = RegistrationForm.objects.create(student_id=self.student_user)
        
        self.all_course_1 = AllCourses.objects.create(
            courseName="Sample Course",
            unit=3,
            type="theory_course"
        )
        
        self.all_course_2 = AllCourses.objects.create(
            courseName="Sample Course 2",
            unit=3,
            type="theory_course"
        )
        
        self.course1 = Course.objects.create(
            course=self.all_course_1,
            teacherName="Dr. Smith",
            isExperimental=False,
            class_time1="شنبه",
            class_time2="دوشنبه",
            class_start_time="10:30:00",
            class_end_time="12:00:00",
            exam_date="2024-12-23",
            exam_start_time="08:00:00",
            exam_end_time="10:00:00",
            capacity=30,
            description="Sample course"
        )
        
        self.course2 = Course.objects.create(
            course=self.all_course_2,
            teacherName="Dr. Smith",
            isExperimental=False,
            class_time1="شنبه",
            class_time2="دوشنبه",
            class_start_time="09:00:00",
            class_end_time="10:30:00",
            exam_date="2024-12-20",
            exam_start_time="08:00:00",
            exam_end_time="10:00:00",
            capacity=30,
            description="Sample course 2"
        )
        
        self.url = "/registration-form/confirm/"
        
        self.client.force_authenticate(user=self.student_user)

    
    def test_confirm_registration_add_courses(self):
        data = {"course_ids": [self.course1.c_id, self.course2.c_id]}
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["msg"], "ok")
        self.assertEqual(response.data["data"], "Courses added successfully")
        selected_courses = SelectedCourse.objects.filter(form=self.form)
        self.assertEqual(selected_courses.count(), 2)
    
    def test_confirm_registration_remove_courses(self):
        SelectedCourse.objects.create(form=self.form, course=self.course1)
        data = {"course_ids": []}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "ok")
        self.assertEqual(response.data["data"], "Courses removed successfully")
        selected_courses = SelectedCourse.objects.filter(form=self.form)
        self.assertEqual(selected_courses.count(), 0)

    def test_confirm_registration_with_invalid_course(self):
        data = {"course_ids": ["INVALID_COURSE"]}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "error")
        self.assertIn("Error in adding courses", response.data["data"])
        
    def test_confirm_registration_no_data(self):
        response = self.client.post(self.url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "ok")
        self.assertEqual(response.data["data"], "Courses removed successfully")
        selected_courses = SelectedCourse.objects.filter(form=self.form)
        self.assertEqual(selected_courses.count(), 0)
    
        
        
        