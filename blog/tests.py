from django.test import TestCase
from django.urls import reverse
from . import forms
from . import models
from django.contrib.auth.models import User

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='uasername')
        cls.post_pub = models.Post.objects.create(
            title='title_pub',
            text='text_pub',
            status='P',
            author=cls.user,
        )
        cls.post_drf = models.Post.objects.create(
            title='title_drf',
            text='text_drf',
            status='D',
            author=cls.user,
        )

    def test_posts_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_posts_list_urlname(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post_pub.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_urlname(self):
        response = self.client.get(reverse('post_detail', args=[self.post_pub.id]))
        self.assertEqual(response.status_code, 200)

    def test_check_posts_list_content_bye_urlname(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post_pub.title)
        self.assertContains(response, self.post_pub.text)
        self.assertContains(response, self.post_pub.author)

    def test_dont_show_drf_in_posts_list_content_bye_urlname(self):
        response = self.client.get(reverse('posts_list'))
        self.assertNotContains(response, self.post_drf.title)
        self.assertNotContains(response, self.post_drf.text)
        self.assertContains(response, self.post_drf.author)

    def test_404_error_if_post_doesnt_exist_bye_url_names(self):
        response_detail = self.client.get(reverse('post_detail', args=[100]))
        response_update = self.client.get(reverse('post_update', args=[100]))
        response_delete = self.client.get(reverse('post_update', args=[100]))

        self.assertEqual(response_detail.status_code, 404)
        self.assertEqual(response_update.status_code, 404)
        self.assertEqual(response_delete.status_code, 404)
    
    def test_check_post_detail_content_bye_urlname(self):
        response = self.client.get(reverse('post_detail', args=[self.post_pub.id]))
        self.assertContains(response, self.post_pub.title)
        self.assertContains(response, self.post_pub.text)
        self.assertContains(response, self.post_pub.author)

    def test_check_post_detail_content_bye_urlname(self):
        response = self.client.get(reverse('post_detail', args=[self.post_pub.id]))
        self.assertContains(response, self.post_pub.title)
        self.assertContains(response, self.post_pub.text)
        self.assertContains(response, self.post_pub.author)

    def test_render_templates_bye_urlnames(self):
        response_detail = self.client.get(reverse('post_detail', args=[self.post_pub.id]))
        response_update = self.client.get(reverse('post_update', args=[self.post_pub.id]))
        response_delete = self.client.get(reverse('post_delete', args=[self.post_pub.id]))
        response_blog = self.client.get(reverse('posts_list'))
        response_create = self.client.get(reverse('post_create'))


        self.assertTemplateUsed(response_detail, 'blog/post_detail.html')
        self.assertTemplateUsed(response_update, 'blog/post_update.html')
        self.assertTemplateUsed(response_delete, 'blog/post_delete.html')
        self.assertTemplateUsed(response_blog, 'blog/posts_list.html')
        self.assertTemplateUsed(response_create, 'blog/post_create.html')

    def test_post_model_str(self):
        post = self.post_pub
        self.assertEqual(str(post), f'{post.author} on {post.datetime_created}')

    def test_post_saved_details(self):
        self.assertEqual(self.post_pub.title, 'title_pub')
        self.assertEqual(self.post_pub.text, 'text_pub')
        self.assertEqual(self.post_pub.status, 'P')
    
    def test_post_create_view(self):
        response = self.client.post(       
            reverse('post_create'),
            {
                'title': 'title',
                'text': 'text',
                'status': 'P',
                'author': self.user.id,
            },
        )
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Post.objects.last().title, 'title')
        self.assertEqual(models.Post.objects.last().text, 'text')
        self.assertEqual(models.Post.objects.last().status, 'P')
        self.assertEqual(models.Post.objects.last().author, self.user)

    def test_post_update_view(self):
        response = self.client.post(       
            reverse('post_update', args=[self.post_drf.id]),
            {
                'title': 'title_up',
                'text': 'text_up',
                'status': 'P',
                'author': self.user.id,
            },
        )
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Post.objects.last().title, 'title_up')
        self.assertEqual(models.Post.objects.last().text, 'text_up')
        self.assertEqual(models.Post.objects.last().status, 'P')
        self.assertEqual(models.Post.objects.last().author, self.user)
    
    def test_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post_drf.id]),)
        self.assertEqual(response.status_code, 302)
