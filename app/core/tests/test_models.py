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

        self.assert_(user.email, email)
        self.assert_(user.check_password(password))