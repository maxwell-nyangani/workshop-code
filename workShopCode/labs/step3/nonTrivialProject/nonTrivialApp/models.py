from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
    rating = models.IntegerField()

    class Meta:
        ordering = ("date_created",)
