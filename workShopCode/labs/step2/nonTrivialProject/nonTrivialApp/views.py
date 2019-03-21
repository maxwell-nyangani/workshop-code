from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

from nonTrivialApp.models import Store
from nonTrivialApp.serializers import StoreSerializer

# dont forget the "id" param that comes from the path.


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_store(request, id):
    return Response({})


@api_view(['GET', 'POST'])
def get_post_stores(request):
    return Response({})
