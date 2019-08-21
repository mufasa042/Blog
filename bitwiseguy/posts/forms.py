from django import forms
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from ckeditor.widgets import CKEditorWidget
from .models import Category, Article

class create_article_form(forms.ModelForm):
    class Meta:
        model = Article
        #fields = ['title', 'content',]
        fields = ('title', 'content', 'categories', 'pub_date')
        labels = {
                'titel': 'Title',
                'categories': 'Categories',
                }
        widgets = {
                'content': CKEditorWidget(),
                }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(create_article_form, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # Get the unsaved Pizza instance
        instance = forms.ModelForm.save(self, False)
        instance.author = self.user
        #instance.pub_date = timezone.now()

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            # This is where we actually link the pizza with toppings
            instance.categories.clear()
            for category in self.cleaned_data['categories']:
                instance.categories.add(category)

        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        # Just like this
        # if commit:
        instance.save()
        self.save_m2m()

        return instance
