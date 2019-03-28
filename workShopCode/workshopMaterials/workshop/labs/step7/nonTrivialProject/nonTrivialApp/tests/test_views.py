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
