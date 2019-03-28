from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from nonTrivialApp.models import Store
from nonTrivialApp.serializers import StoreSerializer
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics
from nonTrivialApp.models import Store, Tag
from nonTrivialApp.serializers import StoreSerializer, TagSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.utils.html import escape
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from nonTrivialApp.models import Customer, Address

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
@permission_classes((IsAuthenticated, ))
def get_post_store(request):
    # get all stores in the system
    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)
    # insert a new record for a store
    elif request.method == 'POST':
        return Response({})

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