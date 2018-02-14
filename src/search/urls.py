from django.conf.urls import url


# relative import from product.views
from .views import (
    SearchProductView,
    
    )

urlpatterns = [
    url(r'^$', SearchProductView.as_view(), name='query'),
]
