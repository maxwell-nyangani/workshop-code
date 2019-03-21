from django.conf.urls import url
from nonTrivialApp import views

urlpatterns = [
    url(
        r'^api/v1/stores/(?P<id>[0-9]+)$',
        views.get_delete_update_store,
        name='get_delete_update_store'
    ),
    url(
        r'^api/v1/stores/$',
        views.get_post_stores,
        name='get_post_stores'
    )
]
