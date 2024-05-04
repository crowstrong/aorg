from django.forms import ValidationError
from django.test import TransactionTestCase
from faker import Faker

from core.models import CustomUserModel


class UserModelTestCase(TransactionTestCase):
    def tearDown(self):
        """
        Clean up the database after each test.
        """
        CustomUserModel.objects.all().delete()

    def test_phone_number_format(self):
        """
        Test that phone numbers must start with "+32".
        """
        faker = Faker()

        # Create a user with a valid phone number
        user1 = CustomUserModel.objects.create(
            username=faker.word(),  # Unique username
            name=faker.word(),
            surname=faker.word(),
            email=faker.email(),
            phone_number="+32456789012",  # Valid phone number
            national_number="00.00.00-000.00",  # Valid national number
            gender=faker.random_element(["Male", "Female", "NA"]),
            birth_date=faker.date_of_birth(),
        )
        # Check that the user was created successfully
        self.assertIsNotNone(user1)

        # Create a user with an invalid phone number
        with self.assertRaises(ValidationError):
            user2 = CustomUserModel.objects.create(
                username=faker.word(),  # Unique username
                name=faker.word(),
                surname=faker.word(),
                email=faker.email(),
                phone_number="1234567890",  # Invalid phone number
                national_number="00.00.00-000.00",  # Valid national number
                gender=faker.random_element(["Male", "Female", "NA"]),
                birth_date=faker.date_of_birth(),
            )
