from django.contrib import admin
from nonTrivialApp.models import Store  # Import your model here.
# Register your models here.
admin.site.register(Store)  # This make your model accessible from admin portal
