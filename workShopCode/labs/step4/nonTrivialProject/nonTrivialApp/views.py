from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

from nonTrivialApp.models import Store
from nonTrivialApp.serializers import StoreSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_store(request, id):
    # dont forget the "id" param that comes from the path.

    # get the record that will be processed by this request if it exists
    try:
        store = Store.objects.get(id=id)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single store
    if request.method == 'GET':
        serializer = StoreSerializer(store)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_post_stores(request):
    # get all stores in the system
    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)
    # insert a new record for a store
    elif request.method == 'POST':
        return Response({})
