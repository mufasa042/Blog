# A dictionary with app names as keys and their 
# respective pip packages as values
app_packages = {
        'ckeditor': 'django-ckeditor',
        'ckeditor_uploader': '',
        'rest_framework': 'django-rest',
        'rest_framework.authtoken':'',
        'rest_auth': 'django-rest-auth',

        }

apps = [app for app in app_packages.keys()] 
packages = [package for package in app_packages.values()]
