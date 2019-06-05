from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.base_view, name = 'base'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.category_view, name = 'category_detail'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', views.product_view, name = 'product_detail'),

]
