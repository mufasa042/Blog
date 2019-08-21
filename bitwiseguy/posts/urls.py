from django.urls import path
from .views import (
        home_view,
        article_detail,
        create_article_view,
        about,
        )
app_name = 'posts'

urlpatterns = [
        path('', home_view, name = 'home' ),
        path('articles/<str:slug>', article_detail, name = 'detail'),
        path('compose/', create_article_view, name = 'compose'),
        path('about/', about, name = 'about'),
        ]
