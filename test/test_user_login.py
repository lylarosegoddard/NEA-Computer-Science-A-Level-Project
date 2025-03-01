import unittest
from app.models.user import User

class TestUserLogin(unittest.TestCase):
    def tearDown(self):
        User.delete().execute()

    def test_successful_login(self):
        user = User(name = "testuser")
        user.set_password('testpassword')
        self.assertEqual(user.name, 'testuser')
        self.assertTrue(user.check_password('testpassword'))
        
    def test_failed_login(self):
        user = User(name = "testuser2")
        user.set_password('testpassword')
        self.assertEqual(user.name, 'testuser2')
        self.assertFalse(user.check_password('wrongpassword'))