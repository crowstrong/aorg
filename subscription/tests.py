from datetime import date, timedelta

from django.test import TestCase
from django.utils import timezone
from faker import Faker

from core.models import CustomUserModel
from subscription.models import Subscription


class SubscriptionModelTest(TestCase):
    def tearDown(self):
        """
        Clean up the database after each test.
        """
        Subscription.objects.all().delete()

    def setUp(self):
        faker = Faker()
        self.user = CustomUserModel.objects.create_user(
            username=faker.word(),  # Unique username
            name=faker.word(),
            surname=faker.word(),
            email=faker.email(),
            phone_number="+32456789012",  # Valid phone number
            national_number="00.00.00-000.00",  # Valid national number
            gender=faker.random_element(["Male", "Female", "NA"]),
            birth_date=faker.date_of_birth(),
        )

    def test_subscription_end_date(self):
        """
        Test whether the end date of the subscription is set correctly based on the subscription type.
        """
        # Create a subscription for 1 month
        subscription_1_month = Subscription.objects.create(
            user=self.user, subscription_type="individual_1_month", price=29.99, start_date=timezone.now()
        )
        # Check if the end date is set to 30 days from the start date
        expected_end_date = subscription_1_month.start_date + timedelta(days=30)
        self.assertEqual(subscription_1_month.end_date.date(), expected_end_date)

        # Create a subscription for 1 year
        subscription_1_year = Subscription.objects.create(
            user=self.user, subscription_type="individual_1_year", price=199.99, start_date=timezone.now()
        )
        # Check if the end date is set to 365 days from the start date
        expected_end_date = subscription_1_year.start_date + timedelta(days=365)
        self.assertEqual(subscription_1_year.end_date.date(), expected_end_date)

    def test_subscription_is_active(self):
        """
        Проверка активности подписки на основе даты окончания.
        """
        # Создание подписки на 1 месяц
        subscription_1_month = Subscription.objects.create(
            user=self.user, subscription_type="individual_1_month", price=29.99, start_date=timezone.now()
        )

        # Проверка, что подписка активна
        self.assertTrue(subscription_1_month.is_active)

        # Установка даты окончания на 26 мая 2024 года
        end_date = subscription_1_month.start_date + timedelta(days=31)
        subscription_1_month.end_date = end_date
        subscription_1_month.save()

        # Приведение всех дат к одному типу перед сравнением
        today = date.today()

        # Проверка, что подписка не активна после 26 мая 2024 года
        self.assertFalse(today > subscription_1_month.end_date)
