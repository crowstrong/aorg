from django.test import TransactionTestCase
from django.utils import timezone
from faker import Faker

from post.models import Post


class PostModelTest(TransactionTestCase):
    def tearDown(self):
        """
        Clean up the database after each test.
        """
        Post.objects.all().delete()

    def test_str_method(self):
        faker = Faker()
        title = faker.sentence()
        post = Post.objects.create(
            title=title,
            content=faker.paragraph(),
            slug=faker.slug(),
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )
        self.assertEqual(str(post), title)

    def test_ordering(self):
        faker = Faker()
        post1 = Post.objects.create(
            title=faker.sentence(),
            content=faker.paragraph(),
            slug=faker.slug(),
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )
        post2 = Post.objects.create(
            title=faker.sentence(),
            content=faker.paragraph(),
            slug=faker.slug(),
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )

        posts = Post.objects.all()
        self.assertEqual(posts[0], post2)
        self.assertEqual(posts[1], post1)

    def test_unique_slug(self):
        faker = Faker()
        # Creating a post with a unique slug
        post1 = Post.objects.create(
            title=faker.sentence(),
            content=faker.paragraph(),
            slug="test-post-1",
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )
        # Creating a post with the same slug
        with self.assertRaises(Exception):
            Post.objects.create(
                title=faker.sentence(),
                content=faker.paragraph(),
                slug="test-post-1",  # Same slug as the first post
                created_at=timezone.now(),
                updated_at=timezone.now(),
            )
