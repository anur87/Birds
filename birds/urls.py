from django.template.defaulttags import url
from django.urls import path

from birds import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('blog', views.blog, name='blog'),
    path('single/<int:pk>/', views.single, name='single'),

    path('search', views.search, name='search'),
    path('article_list', views.article_list, name='article_list'),
    path('add_comment/<int:pk>', views.add_comment, name='add_comment'),
    path('feedback_form', views.feedback_form, name='feedback_form'),

    path('send_message', views.send_message, name='send_message'),
    path('register', views.register, name='register'),
    path('add_user', views.add_user, name='add_user'),
    path('success_register', views.success_register, name='success_register'),
    path('success_auth', views.success_auth, name='success_auth'),
    path('user_login', views.user_login, name='user_login'),
    path(r'delete_comment/<int:id>', views.delete_comment, name='delete_comment'),
    path('articles_filter', views.articles_filter, name='articles_filter'),

    #path('article/<slug:slug>', views.article, name='article'),
]