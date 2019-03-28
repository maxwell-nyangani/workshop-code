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
    ),
    url(
        r'^api/v1/products/$',
        views.get_post_products,
        name='get_post_products'
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
