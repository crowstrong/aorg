from django.test import TestCase

from userprofiles.factories import CustomUserModelFactory
from userprofiles.models import Documents, UserProfile


class UserProfileModelTest(TestCase):
    def tearDown(self):
        """
        Clean up the database after each test.
        """
        UserProfile.objects.all().delete()

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = CustomUserModelFactory()

    def setUp(self):
        self.user_profile = UserProfile.objects.create(user=self.user, avatar=None)

    def test_user_profile_creation(self):
        self.assertTrue(isinstance(self.user_profile, UserProfile))
        self.assertEqual(self.user_profile.__str__(), f"Profile of {self.user.username}")


class DocumentsModelTest(TestCase):
    def tearDown(self):
        """
        Clean up the database after each test.
        """
        Documents.objects.all().delete()

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = CustomUserModelFactory()

    def setUp(self):
        self.documents = Documents.objects.create(user=self.user, file=None)

    def test_document_creation(self):
        self.assertTrue(isinstance(self.documents, Documents))
        self.assertEqual(self.documents.__str__(), f"None uploaded by {self.user.username}")
