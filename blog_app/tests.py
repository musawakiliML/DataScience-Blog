from django.test import TestCase, SimpleTestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post
from datetime import datetime

# Create your tests here.
# class SimpleTests(SimpleTestCase):
#     def test_home_page_status_code(self):
#         response = self.client.get("/")
#         self.assertEqual(response.status_code, 200)
#     def test_about_page_status_code(self):
#         response = self.client.get("/about/")
#         self.assertEqual(response.status_code, 200)

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "testuser",
            email = "test@email.com",
            password = "secret"
        )

        self.post = Post.objects.create(
            title = "A Good Title",
            slug = "a-good-title",
            author = self.user,
            body = "Nice Body Content",
            status = "published"
        )
    def test_string_representation(self):
        post = Post(title="A Sample Title")
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A Good Title')
        self.assertEqual(f'{self.post.slug}', 'a-good-title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice Body Content')
        self.assertEqual(f'{self.post.status}', 'published')
    
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice Body Content')
        self.assertTemplateUsed(response, 'index.html')
    
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A Good Title')
        self.assertTemplateUsed(response, 'post.html')
        