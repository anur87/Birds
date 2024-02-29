

from django.test import TestCase
from django.utils import timezone

from birds.models import Articles, FeedBackForm


class FeedBackFormModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        FeedBackForm.objects.create(name='Main')

    def test_name_max_length(self):
        obj = FeedBackForm.objects.get(id=1)
        max_length = obj._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)

    def test_name_verbose_name(self):
        obj = FeedBackForm.objects.get(id=1)
        verbose_name = obj._meta.get_field('name').verbose_name
        self.assertEqual(verbose_name, 'Имя отправителя')

    def test_message_verbose_name(self):
        obj = FeedBackForm.objects.get(id=1)
        verbose_name = obj._meta.get_field('message').verbose_name
        self.assertEqual(verbose_name, 'Сообщение')

    def test_status_choices(self):
        STATUSES = [
            ('PRO', 'Обработано'),
            ('NOT', 'Не обработано')
        ]
        obj = FeedBackForm.objects.get(id=1)
        self.assertTrue(obj._meta.get_field('status').choices, STATUSES)













