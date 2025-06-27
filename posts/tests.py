from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title = "Test Post", content = "This is a test post")

    def test_post_has_title(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')
    
    def test_post_has_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.content, 'This is a test post')

class PostViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title = "Test Post", content = "This is a test post")
    
    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('post_detail', 
                                           args=[str(post.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, "This is a test post")

    def test_post_update_view(self):
        post = Post.objects.get(id=1)
        
        response = self.client.post(reverse('post_update',
                                    args = [str(post.id)]),
                                   {'title': 'Edited Post', 'content': 'This is an edited post'})
        edit_post = Post.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(edit_post.title, 'Edited Post')
        self.assertContains(edit_post.content, 'This is an edited post')

    def test_post_delete_view(self):
        post = Post.objects.get(id=1)
        response = self.client.post(reverse('post_delete',
                                            args = [str(post.id)]))
        self.assertEqual(response.status_code, 302)
