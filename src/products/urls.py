from django.conf.urls import url


# relative import from product.views
from .views import (
    ProductListView,
    ProductDetailSlugView,
    #product_list_view, 
    #ProductDetailView, 
    #product_detail_view,
    #ProductFeaturedListView,
    #ProductFeaturedDetailView,
    )

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]
