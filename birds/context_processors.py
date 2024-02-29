from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from birds.forms import SearchForm, FeedBackModelForm, RegisterForm, LoginForm, CommentForm, CommentModelForm
from birds.models import Comment, Articles


def add_default_data(request):
    comments_footer = Comment.objects.all()[:3]
    articles_footer = Articles.objects.all()[:3]
    search_form = SearchForm()
    feedback_model_form = FeedBackModelForm()
    register_form = RegisterForm()
    login_form = LoginForm()
    comment_form = CommentForm()
    form = CommentModelForm()
    comments = Comment.objects.all()
    return {'comments_footer': comments_footer, 'articles_footer': articles_footer, 'search_form': search_form,
            'feedback_model_form': feedback_model_form, 'register_form':  register_form, 'login_form': login_form,
            'comment_form': comment_form, 'form': form,  'comments': comments}
