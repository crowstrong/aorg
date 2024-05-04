import factory
from django.core.exceptions import ValidationError
from django.test import TestCase
from faker import Faker

from core.models import CustomUserModel
from userprofiles.models import Documents, UserProfile


class CustomUserModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUserModel

    name = factory.Faker("first_name")
    surname = factory.Faker("last_name")
    email = factory.Faker("email")
    phone_number = "+32456789012"
    national_number = factory.Faker("numerify", text="##.##.##-###.##")
    gender = factory.Faker("random_element", elements=["Male", "Female", "NA"])
    birth_date = factory.Faker("date_of_birth")

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """
        Override the default _create method to add custom validation logic.
        """
        try:
            return super()._create(model_class, *args, **kwargs)
        except ValidationError as e:
            raise ValueError(f"Invalid data: {e}")


class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Documents

    user = factory.SubFactory(CustomUserModelFactory)
    file = factory.django.FileField(filename="test_document.docx")


class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(CustomUserModelFactory)
    avatar = factory.django.ImageField(filename="avatar.jpg")
    documents = factory.RelatedFactoryList(DocumentFactory, size=3)


class TestUserProfile(TestCase):
    def setUp(self):
        self.user_profile = UserProfileFactory()

    def test_user_profile_creation(self):
        self.assertTrue(UserProfile.objects.exists())

    def test_avatar_upload(self):
        self.assertTrue(self.user_profile.avatar)

    def test_document_creation(self):
        self.assertEqual(self.user_profile.documents.count(), 3)
