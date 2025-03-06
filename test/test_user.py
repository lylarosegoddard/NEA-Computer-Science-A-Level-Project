#TestUserLogin class - TDD

import unittest
from app.models.user import User
from app.models.message import Message
from app.models.conversation import Conversation
from app.peewee import initialise_database
#initialises the database and creates tables within the database

class TestUserLogin(unittest.TestCase):
    def setUp(self):
        initialise_database()
        self.user = User(name = "testuser")
        self.user.set_password('testpassword')
        self.user.save()
    #sets up the test by creating the database with a test user and password which are saved to the database
        
    def tearDown(self):
        Message.delete().execute()
        Conversation.delete().execute()
        User.delete().execute()
    #deletes the database

    def test_successful_login(self):
        self.assertTrue(self.user.check_password('testpassword'))
    #user logs in with the correct password and the system checks if the password is correct
        
    def test_failed_login(self):
        self.assertFalse(self.user.check_password('wrongpassword'))
    #user logs in with the wrong password and the system checks if the password is correct

