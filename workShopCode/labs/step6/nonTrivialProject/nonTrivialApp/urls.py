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
    ),
    url(
        r'^api/v1/create-customer/$',
        views.create_customer,
        name='create_customer'
    ),

    url(
        r'^api/v1/authenticate-customer/$',
        views.authenticate_customer,
        name='authenticate_user'
    ),
    url(
        r'^api/v1/addresses/$',
        views.get_post_addresses,
        name='get_post_addresses'
    )
]
