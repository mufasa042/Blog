from django.contrib import admin
from .models import Article, Category, SiteSettings

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(SiteSettings)
