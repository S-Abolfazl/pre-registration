from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User
from .models import AllCourses, Course

class CourseCreateTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="400243068", password="password", email="h@example.com", type="academicassistant")
        self.client.force_authenticate(user=self.user)
        
        
        self.all_course = AllCourses.objects.create(
            courseName="Sample Course",
            unit=3,
            type="theory_course"
        )
        
        self.valid_payload = {
            "course": str(self.all_course.course_id),
            "teacherName": "Dr. Smith",
            "isExperimental": False,
            "class_time1": "شنبه",
            "class_time2": "دوشنبه",
            "class_start_time": "10:30:00",
            "class_end_time": "12:00:00",
            "exam_date": "2024-12-20",
            "exam_start_time": "08:00:00",
            "exam_end_time": "10:00:00",
            "capacity": 30,
            "description": "This is a sample course description."
        }
        
        self.invalid_payload = {
            "course": "invalid-course-id",
            "teacherName": "",
            "capacity": -10
        }
        
    def test_create_course_success(self):
        response = self.client.post("/course/create-courses-in-term/", self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("data", response.data)
        self.assertIn("msg", response.data)
        self.assertEqual(response.data["msg"], "ok")
        
        self.assertEqual(Course.objects.count(), 1)
        created_course = Course.objects.first()
        self.assertEqual(created_course.teacherName, "Dr. Smith")
        self.assertEqual(created_course.capacity, 30)
            
    def test_create_course_failure_invalid_data(self):
        response = self.client.post("/course/create-courses-in-term/", self.invalid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("data", response.data)
        self.assertIn("msg", response.data)
        self.assertEqual(response.data["msg"], "error")
        
        self.assertEqual(Course.objects.count(), 0)

