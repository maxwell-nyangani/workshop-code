# workshop-code
The Practical Guide.

Snippet 1

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

Snippet 2

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


Snippet 3

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Snippet 5

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

Snippet 6

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

Snippet 7

```python
from django.contrib import admin
from nonTrivialApp.models import Store  # Import your model here.
# Register your models here.
admin.site.register(Store) # This make your model accessible from admin portal
```

Snippet 8

```python
from rest_framework import serializers
from nonTrivialApp.models import Store
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

    #user = UserSerializer(read_only=True)

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
```

Snippet 9

```python
from django.conf.urls import url
from nonTrivialApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.static import serve

@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)



urlpatterns = [
    url(
        r'^api/v1/stores/(?P<id>[0-9]+)$',
        views.get_delete_update_store,
        name='get_delete_update_store'
    ),
    url(
        r'^api/v1/stores/$',
        views.get_post_store,
        name='get_post_store'
    )
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


```

Snippet 10

```python
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

# dont forget the "id" param that comes from the path.
@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_store(request, id):
    return Response({})

@api_view(['GET', 'POST'])
def get_post_store(request):
    return Response({})

```

Snippet 11

```python
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('nonTrivialApp.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

```

Snippet 12

```python
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from nonTrivialApp.models import Store
from nonTrivialApp.serializers import StoreSerializer
from django.contrib.auth.models import User

# initialize the APIClient app, This client will be used to send HTTP requests to the API itself and it returns the Response of the API
client = Client()

class GetAllStoresTest(TestCase):
    """ Test module for GET all Stores API view function """

    def setUp(self):  # this is used to create the preconditions before the test
        user1 = User.objects.create_user(username='a', email='a@a.a')
        Store.objects.create(
            user=user1,
            name='Store1',
            rating=0)
        user2 = User.objects.create_user(username='b', email='b@b.b')
        Store.objects.create(
            user=user2,
            name='Store2',
            rating=0)

    def test_get_all_stores(self):
        # get API response
        response = client.get(reverse('get_post_store'))
        # get data from db
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

```

Snippet 13

```python
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from nonTrivialApp.models import Store
from nonTrivialApp.serializers import StoreSerializer
# Create your views here.

@api_view(['GET', 'DELETE', 'PUT'])
# dont forget the "id" param that comes from the path.
def get_delete_update_store(request, id):
    return Response({})

@api_view(['GET', 'POST'])
def get_post_store(request):
    # get all stores in the system
    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)
    # insert a new record for a store
    elif request.method == 'POST':
        return Response({})

```

```python
from rest_framework import serializers
from nonTrivialApp.models import Store
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

    user = UserSerializer(read_only=True) #<<<<<this embeds the data of user

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
```

```python
class GetSingleStoreTest(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='c', email='c@c.c')
        self.jumbo = Store.objects.create(
            user=user1,
            name='Jumbo',
            rating=3)

    def test_get_valid_single_store(self):
        response = client.get(
            reverse('get_delete_update_store', kwargs={'id': self.jumbo.id})
        )
        store = Store.objects.get(id=self.jumbo.id)
        serializer = StoreSerializer(store)
        self.assertEqual(
            response.data,
            serializer.data,
            'The response data does not match the serializer data'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            'The response code was not 200'
        )

```

```python
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from nonTrivialApp.models import Store
from nonTrivialApp.serializers import StoreSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET', 'DELETE', 'PUT'])
# dont forget the "id" param that comes from the path.
def get_delete_update_store(request, id):
    # get the record that will be processed by this request if it exists
    try:
        store = Store.objects.get(id=id)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single store
    if request.method == 'GET':
        serializer = StoreSerializer(store)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        return Response({})
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_store(request):
    # get all stores in the system
    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)
    # insert a new record for a store
    elif request.method == 'POST':
        return Response({})
```

```python
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

```

```python
from django.contrib import admin
# Import your models here.
from nonTrivialApp.models import Store, Address, Customer, Delivery, Product, Purchase, PurchaseItem, Tag
# Register your models here.
admin.site.register(Store)  # This make your model accessible from admin portal
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Delivery)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(PurchaseItem)
admin.site.register(Tag)

```

```python
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

```

```python
urlpatterns = [
    url(
        r'^api/v1/stores/(?P<id>[0-9]+)$',
        views.get_delete_update_store,
        name='get_delete_update_store'
    ),
    url(
        r'^api/v1/stores/$',
        views.get_post_store,
        name='get_post_store'
    ),
    url(
        r'^api/v1/tags/(?P<pk>[0-9]+)/$',
        views.TagDetail.as_view(),
        name='get_post_stores'
    ),
    url(
        r'^api/v1/tags/$',
        views.TagList.as_view(),
        name='get_post_stores'
    )
]

```

```python
from rest_framework import mixins
from rest_framework import generics
from nonTrivialApp.models import Store, Tag
from nonTrivialApp.serializers import StoreSerializer, TagSerializer
```

```python
class TagList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TagDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
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
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
```

```python
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def get_post_stores(request):
    # get all stores in the system
    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)
    # insert a new record for a store
    elif request.method == 'POST':
        return Response({})
```

```python
    ,
    url(
        r'^api/v1/create-customer/$',
        views.create_customer,
        name='create_customer'
    ),

    url(
        r'^api/v1/authenticate-customer/$',
        views.authenticate_customer,
        name='authenticate_user'
    )
 ```

```python
from django.utils.html import escape
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from nonTrivialApp.models import Customer, Address
```

```python
@api_view(['POST'])
def create_customer(request):
    try:
        username = escape(request.POST["username"])
        email = escape(request.POST["email"])
        password = escape(request.POST["password"])
    except:
        return Response({
            'error': 'missing form data'
        })

    gender = escape(request.POST.get("gender", "-"))
    line_1 = escape(request.POST.get("line_1", "-"))
    line_2 = escape(request.POST.get("line_2", "-"))
    city = escape(request.POST.get("city", "-"))
    country = escape(request.POST.get("country", "-"))
    lat = escape(request.POST.get("lat", '0'))
    lon = escape(request.POST.get("lon", '0'))

    # check username taken
    user = User.objects.filter(username=username)
    if len(user) > 0:
        return Response({"error": "username taken"})

    # check email taken
    user = User.objects.filter(email=email)
    if len(user) > 0:
        return Response({"error": "email taken"})

    # create user
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email
    )
    token = Token.objects.create(user=user)

    # create the Address of the customer
    customer_address = Address(
        line_1=line_1,
        line_2=line_2,
        city=city,
        country=country,
        lat=lat,
        lon=lon
    )
    customer_address.save()

    # adding the user object and the address object to build customer object
    customer = Customer(
        user=user,
        gender=gender,
        address=customer_address
    )
    customer.save()

    return Response({
        'token': str(token)
    })

@api_view(['POST'])
def authenticate_customer(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = User.objects.filter(username=username)
    if len(user) > 0:  # username correct
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': str(token)
            })
        else:
            return Response({
                'error': 'wrong password'
            })
    else:
        return Response({
            'error': 'wrong username'
        })
```

```python
from nonTrivialApp.serializers import AddressSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
```

```python
@api_view(['GET', 'POST'])
def get_post_addresses(request):
    # get all addresses in the system
    if request.method == 'GET':
        address_list = Address.objects.all()

        # paging code
        page_number = request.GET.get("page_number", 1)
        items_per_page = request.GET.get("items_per_page", 5)
        paginator = Paginator(address_list, items_per_page)
        try:
            addresses = paginator.page(
                int(page_number))
        except PageNotAnInteger:
            addresses = paginator.page(1)
        except EmptyPage:
            addresses = paginator.page(
                paginator.num_pages)

        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)
    # insert a new record for a store
    elif request.method == 'POST':
        data = {
            'line_1': request.data.get('line_1'),
            'line_2': request.data.get('line_2'),
            'city': request.data.get('city'),
            'country': request.data.get('country'),
            'lat': request.data.get('lon'),
            'lon': request.data.get('lat')
        }
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

```python
    ,
    url(
        r'^api/v1/addresses/$',
        views.get_post_addresses,
        name='get_post_addresses'
    ),
```

```python
from django.db.models import F
from django.db.models import Q
from nonTrivialApp.models import Product, Tag
from nonTrivialApp.serializers import ProductSerializer

```

```python
@api_view(['GET', 'POST'])
def get_post_products(request):

    if request.method == 'POST':
        # create products
        product1 = Product(
            name="Product1",
            description="Product 1 description",
            price=100,
        )
        product1.save()

        product2 = Product(
            name="Product2",
            description="Product 2 description",
            price=100,
        )
        product2.save()

        # create tags
        tag1 = Tag(name='Tag 1')
        tag1.save()
        tag2 = Tag(name='Tag 2')
        tag2.save()
        tag3 = Tag(name='Tag 3')
        tag3.save()
        tag4 = Tag(name='Tag 4')
        tag4.save()

        product1.tags.add(tag1)
        product1.tags.add(tag2)

        product2.tags.add(tag2)
        product2.tags.add(tag3)
        product2.tags.add(tag4)

        # create tags
        return Response({'message': 'Data created successfully'})
    elif request.method == 'GET':
        products = Product.objects.all()
        # products = Product.objects.filter(tags__name="Tag 1")
        # products = Product.objects.filter(tags__name__in=["Tag 1"])
        # products = Product.objects.all().order_by("name")
        # products = Product.objects.filter(price__gt=500)
        # products = Product.objects.filter(name__icontains="2")
        product_serializer = ProductSerializer(products, many=True)
        
        tags = Tag.objects.all()
        #tags = Tag.objects.filter(product__name="Product2")
        #tags = Tag.objects.filter(product__name="Product1")
        tag_serializer = TagSerializer(tags, many=True)
        return Response({
            'products': product_serializer.data,
            'tags': tag_serializer.data
        })

```

```python
    ,
    url(
        r'^api/v1/products/$',
        views.get_post_products,
        name='get_post_products'
    ),
```


```python 
    ,
    url(
      r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 
      protected_serve, 
      {'document_root': settings.MEDIA_ROOT}
    ),
```

