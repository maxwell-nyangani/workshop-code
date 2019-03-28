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
