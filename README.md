# workshop-code
the code needed to follow along the workshop.

```python
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'nonTrivialApp',
  'rest_framework',
  'rest_framework.authtoken',
]
```




```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
```



```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```





```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'flower_store',
        'USER': 'theUsernameHere',
        'PASSWORD': '<theBatabasePasswordHere>',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

```python
from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="store_relation"
    )
    name = models.CharField(max_length=200, default="Empty Flower Store")
    logo = models.ImageField(
        null=True,
        blank=True,
        upload_to="stores/images/logos/"
    )
    banner = models.ImageField(
        null=True,
        blank=True,
        upload_to="stores/images/banners/"
    )
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=5)

    class Meta:
        ordering = ("date_created",)
```

