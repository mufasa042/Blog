import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from model_utils import Choices
from django.shortcuts import reverse
from django.conf import settings
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

class ArticleManager(models.Manager):
    def published(self):
        now = timezone.now()
        return self.get_queryset().filter(pub_date__lte=now)

class Category(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 200)
    content = RichTextUploadingField()
    slug = models.SlugField(null=True, default = None)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    categories = models.ManyToManyField(Category, default = None)
    TAGS = Choices('Tutorial','Project','Dev Tip')
    tags = models.CharField(choices=TAGS, default=TAGS.Project, max_length=20)
    pub_date = models.DateTimeField(default=timezone.now())
    #TODO add tags
    objects = ArticleManager()

    def save(self, *args, **kwargs):
        title_slug = '-'.join(self.title.lower().split()) 
        self.slug = title_slug
        self.title = self.title.title()
        super(Article,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={id:self.id})

class SiteSettings(models.Model):
    display_picture = models.ImageField(upload_to='media/sitesettings/')
    hero_background = models.ImageField(upload_to='media/sitesettings/')
    default_image = models.ImageField(upload_to='media/sitesettings/')


    def save(self, *args, **kwargs):
        if SiteSettings.objects.exists() and not self.pk:
        # if you'll not check for self.pk
        # then error will also raised in update of exists model
            raise ValidationError('Cannot create multiple instances of site settings')
        return super(SiteSettings, self).save(*args, **kwargs)


    
