from django.test import TestCase
from faker import Faker

from feedback.models import Feedback


class FeedbackModelTest(TestCase):
    def tearDown(self):
        """
        Clean up the database after each test.
        """
        Feedback.objects.all().delete()

    def setUp(self):
        self.fake = Faker()

    def test_feedback_creation(self):
        full_name = self.fake.name()
        phone_number = self.fake.phone_number()
        email = self.fake.email()
        topic = self.fake.random_element(
            elements=("service_info_request", "partnership", "communication_department", "other")
        )
        comment = self.fake.text()

        feedback = Feedback.objects.create(
            full_name=full_name, phone_number=phone_number, email=email, topic=topic, comment=comment
        )

        self.assertEqual(feedback.full_name, full_name)
        self.assertEqual(feedback.phone_number, phone_number)
        self.assertEqual(feedback.email, email)
        self.assertEqual(feedback.topic, topic)
        self.assertEqual(feedback.comment, comment)
