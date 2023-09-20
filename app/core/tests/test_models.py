# tests for models.
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    #Test models.
    def test_create_user_with_email_successful(self):
        #test creating a user with an email is succefull
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    def test_user_email_normalized(self):
        sample_emails = [
            ['test@EXAMPLE.com', 'test@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample1234')
            self.assertEqual(user.email, expected)
