from rest_framework.test import APITestCase
from rest_framework import status

from .models import EducationalChart, CompletedCourses
from user.models import User
from course.models import AllCourses

class EducationalChartCreateApiTest(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create(
            username="admin",
            password="password",
            email="h@example.com",
            type="admin",
            is_staff=True
        )
        
        self.valid_payload = {
            "year": 400,
            "type": "even",
            "units": [],
            "term1": [],
            "term2": [],
            "term3": [],
            "term4": [],
            "term5": [],
            "term6": [],
            "term7": [],
            "term8": []
        }
        
        self.invalid_payload = {
            "year": "",
            "type": "invalid_type",
        }
        
        self.client.force_authenticate(user=self.admin_user)
        self.url = "/student/chart/create/"
        
    def test_create_educational_chart_success(self):
        response = self.client.post(
            self.url,
            data=self.valid_payload,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["msg"], "ok")
        self.assertIn("EducationalChart with id:", response.data["data"])
        
    def test_create_educational_chart_failure(self):
        response = self.client.post(
            self.url,
            data=self.invalid_payload,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "error")
        self.assertIn("data", response.data)
        self.assertIsInstance(response.data["data"], dict)
        
        
class AddCompletedCourseApiTest(APITestCase):
    def setUp(self):
        self.student = User.objects.create(
            username="student",
            password="password",
            email="h@student.com",
            type="student",
            entry_year=400
        )
        
        self.course1 = AllCourses.objects.create(
            courseName="Computer Science 101", unit=3, type="Mandatory"
        )
        self.course2 = AllCourses.objects.create(
            courseName="Computer Science 102", unit=3, type="Mandatory"
        )
        self.course3 = AllCourses.objects.create(
            courseName="Computer Science 103", unit=3, type="Elective"
        )
        
        self.client.force_authenticate(user=self.student)
        self.url = "/student/selecet-passed-course/"
        
    def test_add_completed_courses_success(self):
        data = {
            "course_ids": [self.course1.course_id, self.course2.course_id]
        }
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "درس های انتخاب شده با موفقیت به لیست دروس گذارتده شده اضافه شدند")
        self.assertIn("added_courses", response.data)
        self.assertEqual(len(response.data["added_courses"]), 2)
        self.assertIn("Computer Science 101", response.data["added_courses"])
        self.assertIn("Computer Science 102", response.data["added_courses"])

        self.assertTrue(CompletedCourses.objects.filter(student=self.student, course=self.course1).exists())
        self.assertTrue(CompletedCourses.objects.filter(student=self.student, course=self.course2).exists())
        
    def test_add_completed_courses_empty_list(self):
        data = {
            "course_ids": []
        }
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "error")
        self.assertEqual(response.data["data"], "Course IDs list is required")
        
    def test_add_completed_courses_course_not_found(self):
        data = {
            "course_ids": ["fake1234"]
        }
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["msg"], "Course with ID fake1234 does not exist.")
    