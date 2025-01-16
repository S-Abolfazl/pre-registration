from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User
from course.models import Course, AllCourses


class TestCourse(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test", password="test", type="academic_assistant"
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
        )
        
    def statistics_bar_chart_api_test(self):
        response = self.client.get("academic-assistant/statistics/bar-chart")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "ok")
        self.assertEqual(len(response.data["data"]), 1)
