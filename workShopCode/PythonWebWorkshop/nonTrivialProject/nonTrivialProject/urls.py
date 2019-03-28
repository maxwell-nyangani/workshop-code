from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('nonTrivialApp.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
