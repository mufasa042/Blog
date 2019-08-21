from django.shortcuts import render
from django.views import generic
from .models import Article, Category, SiteSettings
from .forms import create_article_form
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home_view(request):
    published_articles = Article.objects.published().order_by('-pub_date')[:3]
    categories = Category.objects.all()
    settings = SiteSettings.objects.get(pk=1)
    context = {
            'published_articles': published_articles,
            'categories': categories,
            'settings': settings,
            }
    return render(request, 'posts/home.html', context)

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
            'article': article,
            }
    return render(request, 'posts/detail.html', context)

def about(request):
    return render(request, 'posts/about.html')

@login_required
def create_article_view(request):
    form = create_article_form(request.POST or None,user=request.user)
    if form.is_valid():
        new_article = form.save()
        form = create_article_form()
    context = {'form': form}
    return render(request, 'posts/compose.html', context)

