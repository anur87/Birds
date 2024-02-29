from django.test import TestCase
from django.urls import reverse

from birds.forms import FeedBackModelForm
from birds.models import PhotoGallery, Articles, FeedBackForm


class IndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        PhotoGallery.objects.create(photo='abc.jpg')

    def test_200(self):
        response = self.client.get('/birds/')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/birds/')
        self.assertTemplateUsed(response, 'index.html')

    def test_context(self):
        response = self.client.get('/birds/')
        self.assertEqual(len(response.context['photos']), 1)

class BlogViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Articles.objects.create(title='Main', image='abc.png')

    def test_200(self):
        response = self.client.get('/birds/blog')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/birds/blog')
        self.assertTemplateUsed(response, 'blog.html')

    def test_context(self):
        response = self.client.get('/birds/blog')
        self.assertEqual(len(response.context['articles']), 1)

class FeedBackFormViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        FeedBackForm.objects.create(name='Имя')

    def test_200(self):
        response = self.client.get('/birds/contacts')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/birds/contacts')
        self.assertTemplateUsed(response, 'contacts.html')

    def test_name(self):
        data = {'name': 'Имя', 'email': 'test@test.com', 'subject': 'Тема сообщения', 'message': 'Текст сообщения'}
        feedback_form = FeedBackModelForm(data=data)
        self.assertTrue(feedback_form.is_valid())


