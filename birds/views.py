from random import random

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render , get_object_or_404 , redirect
from django.template.loader import get_template
from django.urls import reverse
from django.utils import timezone

from django.views import generic

from birds.forms import SearchForm, CommentForm, FeedBackModelForm, RegisterForm, LoginForm, CommentModelForm
from birds.models import PhotoGallery, Articles, Comment, FeedBackForm

def index(request):
    photos = PhotoGallery.objects.all()[:12]
    context = {'photos': photos}
    return render(
        request,
        'index.html',
        context=context
    )

def gallery(request):

    all_images = PhotoGallery.objects.all()
    random_images = random.sample(list(all_images), min(9, len(all_images)))

    context = {'random_images': random_images}
    return render(request, 'archive.html', context)

def about(request):
    return render(
        request,
        'about.html'
    )

def contacts(request):
    return render(
        request,
        'contacts.html'
    )

def blog(request):
    articles = Articles.objects.all()
    return render(
        request,
        'blog.html',
        {'articles': articles}
    )

def single(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    comments = Comment.objects.filter(note=article)
    return render(
        request,
        'single.html',
        {'article': article, 'comments': comments},
    )

def articles_filter(request):
    article_filter = Articles.objects.filter(date_publicity__lte=timezone.now())
    return render(request, 'blog.html', {'article_filter':  article_filter})


def handler404(request, exception):
    return render(request, '404.html', status=404)

def search(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        q = search_form.cleaned_data['q']
        articles = Articles.objects.filter(
            Q(title__icontains=q) | Q(full_text__icontains=q)
        )
        context = {'articles': articles, 'q': q}
        return render(
            request,
            'blog.html',
            context=context
        )

def article_list(request):
    object_list = Articles.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 5)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {'articles': articles, 'page': page}
    return render(
        request,
        'blog.html',
        context=context
    )

def add_comment(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    comments = Comment.objects.filter(note=article)

    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.note = article
            comment.save()
            return redirect('single', pk=pk)

    else:
        form = CommentModelForm()
    return render(request, 'single.html', {'article': article, 'comments': comments, 'form': form})


#@permission_required('birds.Can delete Комментарий')
def delete_comment(request, id):
    comment_obj = get_object_or_404(Comment, pk=id)
    if comment_obj.author_name == request.user.email:
        comment_obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def feedback_form(request):
    if request.method == 'POST':
        feedback_model_form = FeedBackModelForm(request.POST)
        if feedback_model_form.is_valid():
            feedback_obj = FeedBackForm()
            feedback_obj.name = feedback_model_form.cleaned_data['name']
            feedback_obj.email = feedback_model_form.cleaned_data['email']
            feedback_obj.subject = feedback_model_form.cleaned_data['subject']
            feedback_obj.message = feedback_model_form.cleaned_data['message']
            feedback_obj.save()
            return HttpResponseRedirect(reverse('send_message'))

    else:
        feedback_model_form = FeedBackModelForm()

    context = {'feedback_model_form': feedback_model_form}
    return render(
        request,
        'contacts.html',
        context=context
    )

def send_message(request):
    return render(
        request,
        'send_message.html'
    )

def register(request):
    return render(
        request,
        'register.html'
    )

def add_user(request):

    if request.POST:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            confirm_password = register_form.cleaned_data['confirm_password']

            if password != confirm_password:
                return HttpResponse('Пароли не совпадают')
            elif len(password) <= 6:
                return HttpResponse('Пароль слишком простой')

            elif User.objects.filter(email=email).exists() or User.objects.filter(username=email).exists():
                return HttpResponse('Данный email уже существует')
            else:
                    user = User.objects.create_user(email, email, password)
                    group = Group.objects.get(name='Посетители')
                    user.groups.add(group)
                    user.save()

                    text = get_template('registration/registration_email.html')
                    html = get_template('registration/registration_email.html')

                    context = {'email': email, 'password': password, 'confirm_password': confirm_password}
                    subject = 'Регистрация'
                    from_email = 'from@birds87.kz'

                    text_content = text.render(context)
                    html_content = html.render(context)

                    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
                    msg.attach_alternative(html_content, 'text/html')
                    msg.send()
                    return HttpResponseRedirect(reverse('success_register'))
    else:
        register_form = RegisterForm()

    context = {'register_form': register_form}
    return render(
        request,
        'register.html',
        context=context
    )

def success_register(request):
    return render(
        request,
        'success_register.html'
    )


def user_login(request):
    comment_form = CommentForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if  login_form.is_valid():
            cd =  login_form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('success_auth'))
                else:
                    return HttpResponse('Аккаунт отключен')
            else:
                return HttpResponse('Неверный email пользователя и/или пароль!')
    else:
        login_form = LoginForm()
    return render(request, 'registration/login.html', {'login_form': login_form, 'comment_form': comment_form})


def success_auth(request):
    return render(
        request,
        'success_auth.html'
    )


