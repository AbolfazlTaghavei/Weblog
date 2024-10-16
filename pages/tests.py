from django.test import TestCase
from django.urls import reverse


class PagesTest(TestCase):
    # @classmethod
    # def setUpTestData(cls):
    #     pass

    # def setUp(self):
    #     pass

    def test_home_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_view_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_contactus_view_url(self):
        response = self.client.get('/contactus/')
        self.assertEqual(response.status_code, 200)
    
    def test_home_view_url_name(self):
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)

    def test_home_aboutus_url(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_home_aboutus_url_name(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)

    def test_render_templates_bye_urlnames(self):
        response_aboutus = self.client.get(reverse('about_us'))
        response_contactus = self.client.get(reverse('contact_us'))
        response_home = self.client.get(reverse('home'))
        
        self.assertTemplateUsed(response_aboutus, 'aboutus.html')
        self.assertTemplateUsed(response_contactus, 'contactus.html')
        self.assertTemplateUsed(response_home, 'home.html')

    
