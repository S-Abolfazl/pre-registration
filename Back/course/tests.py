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
            "courseName": str(self.all_course.courseName),
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
            "description": "This is a sample course description.",
            "entry_years": []
        }
        
        self.invalid_payload = {
            "course": "invalid-course-id",
            "teacherName": "",
            "capacity": -10
        }
        
    def test_create_course_success(self):
        valid_payload = self.valid_payload.copy()
        response = self.client.post("/course/create-courses-in-term/", valid_payload, format="json")
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
        self.assertEqual(response.data['data'], "شناسه درس معتبر نیست")
        
        

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
        self.assertIn(f"درس با شناسه:{self.course.c_id} حذف شد", response.data['data'])
        
        self.assertFalse(Course.objects.filter(c_id=self.course.c_id).exists())
    
    def test_delete_nonexistent_course(self):
        invalid_course_id = 99999
        response = self.client.delete(f"/course/delete-course-in-term/{invalid_course_id}")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['msg'], "error")
        self.assertEqual(response.data['data'], "شناسه درس معتبر نیست")
        

class AllCourseCreateApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="400243068", 
            password="Hosein@1382", 
            email="h@example.com", 
            type="academicassistant"
        )
        
        self.client.force_authenticate(user=self.user)
        
        self.valid_payload = {
            "courseName": "Mathematics 101",
            "unit": 3,
            "type": "theory_course"
        }
        self.invalid_payload = {
            "courseName": "",
            "unit": -2,
            "type": "invalid_type"
        }
    
    def test_create_course_success(self):
        response = self.client.post("/course/create/", self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['msg'], "ok")
        self.assertIn("course by id:", response.data['data'])
        
        self.assertEqual(AllCourses.objects.count(), 1)
        created_course = AllCourses.objects.first()
        self.assertEqual(created_course.courseName, "Mathematics 101")
        self.assertEqual(created_course.unit, 3)
        self.assertEqual(created_course.type, "theory_course")
    
    def test_create_course_failure_invalid_data(self):
        response = self.client.post("/course/create/", self.invalid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['msg'], "error")
        self.assertIn("data", response.data)
        
        self.assertEqual(AllCourses.objects.count(), 0)


from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User
from .models import AllCourses

class AllCourseListApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="400243068", 
            password="Hosein@1382", 
            email="h@example.com", 
            type="academicassistant"
        )
        
        self.client.force_authenticate(user=self.user)
                
        self.course1 = AllCourses.objects.create(
            courseName="Mathematics 101",
            unit=3,
            type="theory_course"
        )
        
        self.course2 = AllCourses.objects.create(
            courseName="Physics 101",
            unit=3,
            type="theory_course"
        )
    
    def test_list_all_courses(self):
        response = self.client.get("/course/list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['courseName'], "Mathematics 101")
        self.assertEqual(response.data[1]['courseName'], "Physics 101")
    
    def test_get_course_by_id(self):
        response = self.client.get(f"/course/list/{self.course1.course_id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['courseName'], "Mathematics 101")
        self.assertEqual(response.data['unit'], 3)
    
    def test_get_course_by_id_not_found(self):
        invalid_course_id = "non-existent-course-id"
        response = self.client.get(f"/course/list/{invalid_course_id}")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['msg'], "error")
        self.assertEqual(response.data['data'], "id validation error")


class AllCourseUpdateApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="400243068", 
            password="Hosein@1382", 
            email="h@example.com", 
            type="academicassistant"
        )
        
        self.client.force_authenticate(user=self.user)
        
        self.course = AllCourses.objects.create(
            courseName="Mathematics 101",
            unit=3,
            type="theory_course"
        )
    
    def test_update_course_success(self):
        updated_data = {
            "courseName": "Advanced Mathematics 101",
            "unit": 4,
            "type": "theory_course"
        }
        
        response = self.client.put(f"/course/update/{self.course.course_id}", updated_data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['msg'], "ok")
        self.assertEqual(response.data['data'], f'course by id:{self.course.course_id} updated')
        
        self.course.refresh_from_db()
        self.assertEqual(self.course.courseName, "Advanced Mathematics 101")
        self.assertEqual(self.course.unit, 4)
    
    def test_update_course_not_found(self):
        invalid_course_id = "non-existent-course-id"
        updated_data = {
            "courseName": "Non-existent Course",
            "unit": 4,
            "type": "theory_course"
        }
        
        response = self.client.put(f"/course/update/{invalid_course_id}", updated_data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['msg'], "error")
        self.assertEqual(response.data['data'], "id validation error")
    
    def test_update_course_invalid_data(self):
        invalid_data = {
            "courseName": "Mathematics 101",
            "unit": -3,
            "type": "theory_course"
        }
        
        response = self.client.put(f"/course/update/{self.course.course_id}", invalid_data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['msg'], "error")
        self.assertIn("unit", response.data['data'])
        
        
class AllCourseDeleteApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="400243068", 
            password="Hosein@1382", 
            email="h@example.com", 
            type="academicassistant"
        )
        
        self.client.force_authenticate(user=self.user)        
        
        
        self.course = AllCourses.objects.create(
            courseName="Mathematics 101",
            unit=3,
            type="theory_course"
        )
    
    def test_delete_course_success(self):
        response = self.client.delete(f"/course/delete/{self.course.course_id}")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['msg'], "ok")
        self.assertEqual(response.data['data'], f'course by id:{self.course.course_id} deleted')
        
        with self.assertRaises(AllCourses.DoesNotExist):
            AllCourses.objects.get(course_id=self.course.course_id)
    
    def test_delete_course_not_found(self):
        invalid_course_id = "non-existent-course-id"
        
        response = self.client.delete(f"/course/delete/{invalid_course_id}")
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['msg'], "error")
        self.assertEqual(response.data['data'], "id validation error")
        
        
class CourseinTermApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="400243068", 
            password="Hosein@1382", 
            email="h@example.com", 
            type="academicassistant"
        )
        
        self.client.force_authenticate(user=self.user)  
        
        self.course = AllCourses.objects.create(
            courseName="Mathematics 101",
            unit=3,
            type="theory_course"
        )
        
        self.course_interm = Course.objects.create(
            course=self.course,
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
        
    def test_get_courses_success(self):
        response = self.client.get("/course/courses-in-term/data/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['data'], list)
        self.assertEqual(len(response.data['data']), 1)
        
        course_data = response.data.get('data', [])[0]
        self.assertEqual(course_data['courseName'], "Mathematics 101")
        self.assertEqual(course_data['unit'], 3)
        self.assertEqual(course_data['type'], "theory_course")
        self.assertEqual(course_data['capacity'], 30)
        self.assertEqual(course_data['teacher'], "Dr. Smith")
        self.assertIn("کلاس", course_data['schedule'])
        self.assertIn("امتحان", course_data['schedule'])
        self.assertEqual(course_data['description'], "Sample course")
        
    def test_no_courses_available(self):
        Course.objects.all().delete()
        response = self.client.get("/course/courses-in-term/data/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('data'), [])
    
    def test_access_denied_without_permission(self):
        self.user.type = "support"
        self.user.save()
        response = self.client.get("/course/courses-in-term/data/")
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], "You do not have permission to perform this action.")
    
    def test_get_courses_unauthenticated(self):
        self.client.logout()
        response = self.client.get("/course/courses-in-term/data/")
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "Authentication credentials were not provided.")
        