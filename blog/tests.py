from django.test import TestCase
from blog.models import Post, Comment
from django.utils import timezone

class PostTest(TestCase):
    def create_post(self, author="Samirr Tendulkar", title="blah", text= "blah blah blah"):
        return Post.objects.create(title=title, text=text, author=author, created_date=timezone.now())


    def test_post_creation(self):
        a = self.create_post()
        self.assertTrue(isinstance(a, Post))
        self.assertEqual(a.__str__(), a.title)
