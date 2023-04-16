from django.test import TestCase
from .models import Post
from account.models import CustomUser
import datetime


# Create your tests here.
class BlogTest(TestCase):
    author = CustomUser.objects.get(pk=1)

    def setUp(self):
        user = CustomUser(email='123@yahoo.com', phone_number='09501478559', password='5dfasf5df51654AD684')
        user.save()
        now = datetime.datetime.now()
        post = Post(created_date=now, author=user, title='Unit test1', likes=10, body='djangoo test case',
                    slug='django-test-case')
        post.save()

    def test_blog_works(self):
        post_obj = Post.objects.get(title='Unit test1')
        self.assertEqual(post_obj.title, 'Unit test1')
        self.assertEqual(post_obj.likes, 10)
        self.assertEqual(post_obj.body, 'djangoo test case')
