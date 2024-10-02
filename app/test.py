import unittest
from app.friendclass import Friend

class Friend(unittest.TestCase):
  def test_if_chatbot_interacts_with_user(self):
    friend = Friend("Bob")
    name = friend.complete("Hi there, enter your name:\n")
    self.assertEqual(response,"Hi John, how are you today?")