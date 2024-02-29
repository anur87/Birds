

from django.test import TestCase
from django.utils import timezone

from birds.models import Articles


class ArticleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Articles.objects.create(title='Main')

    def test_title_max_length(self):
        obj = Articles.objects.get(id=1)
        max_length = obj._meta.get_field('title').max_length
        self.assertEqual(max_length, 70)

    def test_title_verbose_name(self):
        obj = Articles.objects.get(id=1)
        verbose_name = obj._meta.get_field('title').verbose_name
        self.assertEqual(verbose_name, 'Название статьи')

    def test_title_unique(self):
        obj = Articles.objects.get(id=1)
        unique = obj._meta.get_field('title').unique
        self.assertTrue(unique)

    def test_author_name_max_length(self):
        obj = Articles.objects.get(id=1)
        max_length = obj._meta.get_field('author_name').max_length
        self.assertEqual(max_length, 70)

    def test_author_name_verbose_name(self):
        obj = Articles.objects.get(id=1)
        verbose_name = obj._meta.get_field('author_name').verbose_name
        self.assertEqual(verbose_name, 'Имя автора')


    def test_text_verbose_name(self):
        obj = Articles.objects.get(id=1)
        verbose_name = obj._meta.get_field('text').verbose_name
        self.assertEqual(verbose_name, 'Описание')

    def test_full_text_verbose_name(self):
        obj = Articles.objects.get(id=1)
        verbose_name = obj._meta.get_field('full_text').verbose_name
        self.assertEqual(verbose_name, 'Полное Описание')

    def test_meta_ordering(self):
        obj = Articles.objects.get(id=1)
        ordering = obj._meta.ordering
        self.assertEqual(ordering, ['id'])

    def test_meta_verbose_name(self):
        obj = Articles.objects.get(id=1)
        verbose_name = obj._meta.verbose_name
        self.assertEqual(verbose_name, 'Статья')

    def test_meta_verbose_name_plural(self):
        obj = Articles.objects.get(id=1)
        verbose_name_plural = obj._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Статьи')

    def test_str(self):
        obj = Articles.objects.get(id=1)
        self.assertEqual(str(obj), obj.title)

    def test_image_upload_to(self):
        obj = Articles.objects.get(id=1)
        self.assertTrue(obj._meta.get_field('image').upload_to, 'images')










