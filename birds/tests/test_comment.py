

from django.test import TestCase
from django.utils import timezone

from birds.models import Articles, Comment


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Articles.objects.create(title='Main')
        Comment.objects.create(
            author_name='author_name',
            note=Articles.objects.get(id=1),
            email='author@gmail.com',
            comment='comment'
        )

    def test_note_null(self):
        obj = Comment.objects.get(id=1)
        self.assertTrue(obj._meta.get_field('note').null)










