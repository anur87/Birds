from django.test import TestCase

from birds.forms import FeedBackModelForm
from birds.models import FeedBackForm


class FeedbackFormTest(TestCase):

    def test_meta_model(self):
        feedback_form = FeedBackModelForm()
        self.assertEqual(feedback_form._meta.model, FeedBackForm)

    def test_meta_fields(self):
        feedback_form = FeedBackModelForm()
        self.assertEqual(feedback_form._meta.fields, ['name', 'email', 'subject', 'message'])

    def test_name_placeholder(self):
        feedback_form = FeedBackModelForm()
        self.assertEqual(feedback_form._meta.widgets['name'].attrs['placeholder'], 'Имя')

    def test_email_placeholder(self):
        feedback_form = FeedBackModelForm()
        self.assertEqual(feedback_form._meta.widgets['email'].attrs['placeholder'], 'E-mail')

    def test_subject_placeholder(self):
        feedback_form = FeedBackModelForm()
        self.assertEqual(feedback_form._meta.widgets['subject'].attrs['placeholder'], 'Тема')

    def test_message_placeholder(self):
        feedback_form = FeedBackModelForm()
        self.assertEqual(feedback_form._meta.widgets['message'].attrs['placeholder'], 'Сообщение')


