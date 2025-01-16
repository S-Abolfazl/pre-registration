from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User
from user.serializers import UserSerializer
from course.models import Course, AllCourses
from registrationForm.models import RegistrationForm
from unittest.mock import patch

class TestBarChart(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test", email="h@g.com", password="test", type="academicassistant"
        )
        self.client.force_authenticate(user=self.user)
        self.all_course = AllCourses.objects.create(
            courseName="test", unit=3, type="theory_course"
        )
        self.course = Course.objects.create(
            course=self.all_course,
            teacherName="test",
            class_time1="شنبه",
            class_time2="دوشنبه",
            class_start_time="08:00",
            class_end_time="10:00",
            capacity=10,
            registered=5,
            isExperimental=False,
        )

    def test_statistics_bar_chart_api_test(self):
        response = self.client.get("/academic-assistant/statistics/bar-chart")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "ok")
        self.assertEqual(len(response.data["data"]), 1)
    
    @patch("course.models.Course.objects.all")
    def test_statistics_bar_chart_api_exception(self, mock_course):
        # Simulate an exception during the query
        mock_course.side_effect = Exception("Database error")

        response = self.client.get("/academic-assistant/statistics/bar-chart")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["msg"], "error")
        self.assertIn("مشکلی در دریافت اطلاعات", response.data["data"])

class TestOverflowedCourses(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test", email="h@g.com", password="test", type="academicassistant"
        )
        self.client.force_authenticate(user=self.user)
        self.all_course = AllCourses.objects.create(
            courseName="test", unit=3, type="theory_course"
        )
        self.course1 = Course.objects.create(
            course=self.all_course,
            teacherName="test 1",
            class_time1="شنبه",
            class_time2="دوشنبه",
            class_start_time="08:00",
            class_end_time="10:00",
            capacity=10,
            registered=15,
            isExperimental=False,
        )

        self.course2 = Course.objects.create(
            course=self.all_course,
            teacherName="test 2",
            class_time1="شنبه",
            class_time2="دوشنبه",
            class_start_time="08:00",
            class_end_time="10:00",
            capacity=10,
            registered=5,
            isExperimental=False,
        )

    def test_statistics_overflowed_courses_api_test(self):
        response = self.client.get("/academic-assistant/statistics/overflowed-courses")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "ok")
        self.assertEqual(len(response.data["data"]), 1)

class TestParticipationPercent(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test", email="h@g.com", password="test", type="academicassistant"
        )
        self.client.force_authenticate(user=self.user)
        
        test_users = [
            {
                "username": "400243020",
                "password": "Hosein@1382",
                "email": "student1@example.com",
                "type": "student",
            },
            {
                "username": "400234021",
                "password": "Hosein@13  ",
                "email": "student2@example.com",
                "type": "student",
            },
            {
                "username": "400243022",
                "password": "Hosein@1382",
                "email": "student3@example.com",
                "type": "student",
            },
            {
                "username": "400243023",
                "password": "Hosein@1382",
                "email": "student4@example.com",
                "type": "student",
            },
            {
                "username": "401243020",
                "password": "Hosein@1382",
                "email": "student8@example.com",
                "type": "student",
            },
            {
                "username": "402243020",
                "password": "Hosein@1382",
                "email": "student12@example.com",
                "type": "student",
            },
            {
                "username": "402234021",
                "password": "Hosein@13  ",
                "email": "student13@example.com",
                "type": "student",
            },
            {
                "username": "403243020",
                "password": "Hosein@1382",
                "email": "student16@example.com",
                "type": "student",
            },
            {
                "username": "403234021",
                "password": "Hosein@13  ",
                "email": "student17@example.com",
                "type": "student",
            },
            {
                "username": "99243020",
                "password": "Hosein@1382",
                "email": "student20@example.com",
                "type": "student",
            },
            {
                "username": "99234021",
                "password": "Hosein@13  ",
                "email": "student21@example.com",
                "type": "student",
            },
        ]
        
        for user_data in test_users:
            serializer = UserSerializer(data=user_data)
            if serializer.is_valid():
                user = serializer.save()

                RegistrationForm.objects.create(student_id=user)
                
    def test_statistics_participation_percent_api_test(self):
        response = self.client.get("/academic-assistant/statistics/participation-percent")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "ok")
        self.assertEqual(len(response.data["data"]), 5)
        
        