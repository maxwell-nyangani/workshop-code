from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)


class Address(models.Model):
    line_1 = models.CharField(max_length=200)
    line_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    lat = models.FloatField(
        null=True,
        blank=True
    )
    lon = models.FloatField(
        null=True,
        blank=True
    )


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="customer_relation"
    )
    gender = models.CharField(max_length=20)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


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


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0)

    # for demonstrating auto many to many field using OODB modeling https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="products/images/"
    )


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sub_total = models.FloatField()


class Delivery(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    destination = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    delivered_on = models.DateTimeField(
        null=True,
        blank=True
    )
