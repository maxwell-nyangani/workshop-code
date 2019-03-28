from rest_framework import serializers
from nonTrivialApp.models import Store, Tag, Address, Customer, Product, Purchase, PurchaseItem, Delivery
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        )

class StoreSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Store
        fields = (
            'id',
            'user',
            'name',
            'logo',
            'banner',
            'is_active',
            'date_created',
            'rating',
        )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'date_created',
        )

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'line_1',
            'line_2',
            'city',
            'country',
            'lat',
            'lon',
        )

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'user',
            'gender',
            'address',
        )

class ProductSerializer(serializers.ModelSerializer):
    # to get the collection of related objects in many to many relationship
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'tags',
            'image',
        )

class PurchaseSerializer(serializers.ModelSerializer):
    # to get the collection of related objects in many to many relationship
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Purchase
        fields = (
            'id',
            'customer',
            'date',
        )

class PurchaseItemSerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Purchase
        fields = (
            'id',
            'purchase',
            'product',
            'quantity',
            'sub_total',
        )

class DeliverySerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer(read_only=True)

    class Meta:
        model = Purchase
        fields = (
            'id',
            'purchase',
            'destination',
            'status',
            'delivered_on',
        )