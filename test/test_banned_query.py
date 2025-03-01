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
        

    def tearDown(self):
        Message.delete().execute()
        Conversation.delete().execute()
        User.delete().execute()

    def test_not_banned_user(self):
        self.assertFalse(BannedQuery(self.user).banned())
    
    def test_banned_user(self):
        conversation = Conversation.create(user=self.user)
        for i in range(3):
            message = Message.create(conversation=conversation, message=f"Bullying message {i}", is_bullying=True)

        
        self.assertTrue(BannedQuery(self.user).banned())
