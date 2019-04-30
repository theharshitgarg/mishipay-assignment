# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
from utils import shopify


def products(request):
    resp = shopify.get_product_request()
    resp = json.loads(resp.content.decode('utf-8'))

    kwargs = locals()
    return render(request, 'inventory/products.html', kwargs)


def products_api(request):
    resp = shopify.get_product_request()
    resp = json.loads(resp.content.decode('utf-8'))

    return JsonResponse(resp)


def orders(request):
    resp = shopify.get_orders_request()
    resp = json.loads(resp.content.decode('utf-8'))
    print(resp)
    kwargs = locals()
    return render(request, 'inventory/orders.html', kwargs)


def new_order(request):
    resp = shopify.get_product_request()
    resp = json.loads(resp.content.decode('utf-8'))

    if request.method == "POST":
        # Send data to server
        pass

    kwargs = locals()
    return render(request, 'inventory/create_order.html', kwargs)


def new_order_api(request):
    if request.method == "POST":
        print(request.POST)
        pass

    kwargs = locals()
    return render(request, 'inventory/create_order.html', kwargs)
