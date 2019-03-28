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