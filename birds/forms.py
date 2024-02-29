from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from django.http import HttpResponseRedirect, request

from birds.models import FeedBackForm, Comment


class SearchForm(forms.Form):
    q = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Поиск'}
        )
    )

class FeedBackModelForm(forms.ModelForm):
    class Meta:
        model = FeedBackForm
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Имя'}),
            'email': EmailInput(attrs={'placeholder': 'E-mail'}),
            'subject': TextInput(attrs={'placeholder': 'Тема'}),
            'message': Textarea(attrs={'placeholder': 'Сообщение'}),
        }

class RegisterForm(forms.Form):

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': 'E-mail'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Пароль'}
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Повторите пароль'}
        )
    )

class LoginForm(forms.Form):

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': 'E-mail'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Пароль'}
        )
    )

class CommentForm(forms.Form):
    name = forms.CharField(disabled=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя'}
        )
    )
    email = forms.EmailField(disabled=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'E-mail'}
        )
    )
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Комментарий'}
        )
    )

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['author_name', 'email',  'comment']

        widgets = {
            'email': TextInput(attrs={'placeholder': 'Email автора'}),
            'author_name': TextInput(attrs={'placeholder': 'Имя автора'}),
            'comment': Textarea(attrs={'placeholder': 'Комментарий'}),
        }












