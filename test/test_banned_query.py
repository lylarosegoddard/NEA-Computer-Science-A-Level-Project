#TestBannedUser class - TDD

import unittest
from app.models.user import User
from app.models.conversation import Conversation
from app.models.message import Message
from app.peewee import initialise_database
from app.banned_query import BannedQuery

class TestBannedUser(unittest.TestCase):
    def setUp(self):
        initialise_database()
        self.user = User(name = "testuser")
        self.user.set_password('testpassword')
        self.user.save()
        #initialises the database and creates a user with a password to test if the user is banned

    def tearDown(self):
        Message.delete().execute()
        Conversation.delete().execute()
        User.delete().execute()
        #cleans up the database after the test

    def test_not_banned_user(self):
        self.assertFalse(BannedQuery(self.user).banned())
        #tests if the user is not banned

    def test_banned_user(self):
        conversation = Conversation.create(user=self.user)
        for i in range(3):
            message = Message.create(conversation=conversation, message=f"Bullying message {i}", is_bullying=True)
        #creates a conversation with 3 bullying messages

        self.assertTrue(BannedQuery(self.user).banned())
        #tests if the user is banned now that there are 3 bullying messages
