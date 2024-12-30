from user.models import User
from registrationForm.models import RegistrationForm
from user.serializers import UserSerializer

def add_test_users():
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
            "username": "400243024",
            "password": "Hosein@1382",
            "email": "student5@example.com",
            "type": "student",
        },
        {
            "username": "400243025",
            "password": "Hosein@1382",
            "email": "student6@example.com",
            "type": "student",
        },
        {
            "username": "400243026",
            "password": "Hosein@1382",
            "email": "student7@example.com",
            "type": "student",
        },
        {
            "username": "401243020",
            "password": "Hosein@1382",
            "email": "student8@example.com",
            "type": "student",
        },
        {
            "username": "401234021",
            "password": "Hosein@13  ",
            "email": "student9@example.com",
            "type": "student",
        },
        {
            "username": "401243022",
            "password": "Hosein@1382",
            "email": "student10@example.com",
            "type": "student",
        },
        {
            "username": "401243023",
            "password": "Hosein@1382",
            "email": "student11@example.com",
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
            "username": "402243022",
            "password": "Hosein@1382",
            "email": "student14@example.com",
            "type": "student",
        },
        {
            "username": "402243023",
            "password": "Hosein@1382",
            "email": "student15@example.com",
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
            "username": "403243022",
            "password": "Hosein@1382",
            "email": "student18@example.com",
            "type": "student",
        },
        {
            "username": "403243023",
            "password": "Hosein@1382",
            "email": "student19@example.com",
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
        {
            "username": "99243022",
            "password": "Hosein@1382",
            "email": "student22@example.com",
            "type": "student",
        },
        {
            "username": "99243023",
            "password": "Hosein@1382",
            "email": "student23@example.com",
            "type": "student",
        }
        
    ]

    for user_data in test_users:
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            user = serializer.save()

            RegistrationForm.objects.get_or_create(student_id=user)

            print(f"User {user.username} and their registration form created successfully.")
        else:
            print(f"Error creating user: {serializer.errors}")

add_test_users()