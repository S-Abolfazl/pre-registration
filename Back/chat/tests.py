from rest_framework.test import APITestCase
from rest_framework import status
from .models import Chat, Message
from user.models import User


class ChatTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1",
            email="h@g.com",
            password="123456",
            type="student",
        )
        
        self.user2 = User.objects.create_user(
            username="user2",
            email="hh@g.com",
            password="123456",
            type="support",
        )
        
        self.chat = Chat.objects.create(
            sender=self.user1,
            receiver=self.user2,
        )
        
        self.message = Message.objects.create(
            content="hello",
            sender=self.user1,
            receiver=self.user2,
            chat=self.chat,
        )
        
        self.client.force_authenticate(user=self.user1)
        
    def test_chat_list(self):
        response = self.client.get('/chat/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        
    def test_chat_detail(self):
        response = self.client.get(f'/chat/detail/{self.chat.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]['id'], str(self.chat.id))
        
    def test_chat_create(self):
        response = self.client.post('/chat/create/', {
            "sender": self.user1.id,
            "receiver": self.user2.id,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["data"]['sender'], self.user1.id)
        self.assertEqual(response.data["data"]['receiver'], self.user2.id)
        
        
    def test_chat_delete(self):
        response = self.client.delete(f'/chat/delete/{self.chat.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'], 'deleted success')
        
        
    def test_message_list(self):
        chat_id = self.chat.id
        response = self.client.post('/chat/get_messages/', {"chat_id": chat_id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        
    def test_message_create(self):
        response = self.client.post('/chat/create_message/', {
            "content": "hello",
            "sender": self.user1.id,
            "receiver": self.user2.id,
            "chat": self.chat.id,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["data"]['content'], 'hello')
        
    def test_message_update(self):
        response = self.client.patch(f'/chat/update_message/{self.message.id}/', {
            "content": "hi",
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]['content'], 'hi')
        
    def test_message_delete(self):
        response = self.client.delete(f'/chat/delete_message/{self.message.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data['msg'], "پیام با موفقیت حذف شد")
    
    