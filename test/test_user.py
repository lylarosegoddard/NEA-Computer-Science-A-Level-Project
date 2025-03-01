import unittest
from app.models.user import User
from app.models.message import Message
from app.models.conversation import Conversation
from app.peewee import initialise_database


class TestUserLogin(unittest.TestCase):
    def setUp(self):
        initialise_database()
        self.user = User(name = "testuser")
        self.user.set_password('testpassword')
        self.user.save()
        
        
    def tearDown(self):
        Message.delete().execute()
        Conversation.delete().execute()
        User.delete().execute()

    def test_successful_login(self):
        self.assertTrue(self.user.check_password('testpassword'))
        
    def test_failed_login(self):
        self.assertFalse(self.user.check_password('wrongpassword'))

