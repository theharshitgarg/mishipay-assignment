from django.conf.urls import url

from inventory import views

urlpatterns = [
    url(r'^products/list', views.products, name='products_list'),
    url(r'^products/new', views.new_product, name='new_product'),
    url(r'^orders/new', views.new_order, name='new_order'),
    url(r'^orders/list', views.orders, name='orders_list'),

    # APIS
    url(r'^api/v1/products/list', views.products, name='products_list_api'),
    url(r'^api/v1/products/new', views.new_order_api, name='new_order_api'),
]
