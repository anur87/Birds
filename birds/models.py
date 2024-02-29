import datetime

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PhotoGallery(models.Model):
    photo = models.ImageField(
        upload_to='images/birds',
        unique=True,
        verbose_name='Наша Галерея'
    )

    class Meta:
        verbose_name = 'Фотогалерея'
        verbose_name_plural = 'Фотогалереи'

    def __str__(self):
        return '{0}'.format(self.photo)

class Articles(models.Model):
    title = models.CharField(max_length=70, unique=True, verbose_name="Название статьи")
    author_name = models.CharField(max_length=70, verbose_name="Имя автора")
    date_publicity = models.DateTimeField(verbose_name='Дата публикации')
    date_created = models.DateTimeField(verbose_name='Дата создания')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    text = models.TextField(verbose_name='Описание')
    full_text = models.TextField(verbose_name='Полное Описание')

    #slug = models.SlugField(max_length=40, verbose_name='Псевдоним', default='')

    class Meta:
        ordering = ['id']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return '{0}'.format(self.title)


class Comment(models.Model):
    note = models.ForeignKey(Articles, default="Статья", on_delete=models.CASCADE, null=True, verbose_name='Статья', related_name='comments')
    date_of_send = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        validators=[MinValueValidator(datetime.datetime)],
        verbose_name='Дата'
    )
    author_name = models.CharField(max_length=30, verbose_name='Имя автора')
    email = models.EmailField()
    comment = models.TextField(verbose_name='Текст комментария')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        #permissions = (('can_delete_comment', 'Возможность удаления комментария'),)

    def __str__(self):
        return '{0} {1}'.format(self.note.text, self.comment)

class FeedBackForm(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя отправителя')
    email = models.EmailField()
    subject = models.CharField(max_length= 70, verbose_name='Тема сообщения', blank=True)
    message = models.TextField(verbose_name='Сообщение')

    STATUSES = [
        ('PRO', 'Обработано'),
        ('NOT', 'Не обработано')
    ]

    status = models.CharField(choices=STATUSES, max_length=3, default='NOT', verbose_name='Статус')

    class Meta:
        verbose_name = 'Форма связи'
        verbose_name_plural = 'Формы связи'

    def __str__(self):
        return '{0}'.format(self.name)