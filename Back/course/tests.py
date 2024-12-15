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



class CourseListTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="400243068", password="password", email="a@b.com:", type="academicassistant")
        self.client.force_authenticate(user=self.user)
        
        self.all_course = AllCourses.objects.create(
            courseName="Sample Course",
            unit=3,
            type="theory_course"
        )
        
        self.course1 = Course.objects.create(
            course=self.all_course,
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
            description="Sample course 1"
        )
        
        self.course2 = Course.objects.create(
            course=self.all_course,
            teacherName="Dr. Johnson",
            isExperimental=True,
            class_time1="سه شنبه",
            class_time2="چهارشنبه",
            class_start_time="14:30:00",
            class_end_time="16:00:00",
            exam_date="2024-12-21",
            exam_start_time="10:00:00",
            exam_end_time="12:00:00",
            capacity=40,
            description="Sample course 2"
        )
        
    def test_list_all_courses(self):
        response = self.client.get("/course/list-courses-in-term/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['teacherName'], "Dr. Smith")
        self.assertEqual(response.data[1]['teacherName'], "Dr. Johnson")
    
    def test_get_single_course(self):
        response = self.client.get(f"/course/list-courses-in-term/{self.course1.c_id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['teacherName'], "Dr. Smith")
        self.assertEqual(response.data['description'], "Sample course 1")
        
    def test_get_nonexistent_course(self):
        response = self.client.get("/course/list-courses-in-term/invalid-id")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['msg'], "error")
        self.assertEqual(response.data['data'], "id validation error")
        
        

class CourseDeleteApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="400243068", 
            password="Hosein@1382", 
            email="h@example.com", 
            type="academicassistant"
        )
        
        self.client.force_authenticate(user=self.user)
        
        self.all_course = AllCourses.objects.create(
            courseName="Sample Course",
            unit=3,
            type="theory_course"
        )
        
        self.course = Course.objects.create(
            course=self.all_course,
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
    
    def test_delete_existing_course(self):
        response = self.client.delete(f"/course/delete-course-in-term/{self.course.c_id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['msg'], "ok")
        self.assertIn(f"course by id:{self.course.c_id} deleted", response.data['data'])
        
        self.assertFalse(Course.objects.filter(c_id=self.course.c_id).exists())
    
    def test_delete_nonexistent_course(self):
        invalid_course_id = 99999
        response = self.client.delete(f"/course/delete-course-in-term/{invalid_course_id}")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['msg'], "error")
        self.assertEqual(response.data['data'], "id validation error")