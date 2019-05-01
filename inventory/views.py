# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
from utils import shopify
from inventory import forms
# from inventory.services import create_product as cp


def products(request):
    resp = shopify.get_product_request()
    resp = json.loads(resp.content.decode('utf-8'))

    kwargs = locals()
    return render(request, 'inventory/products.html', kwargs)


def new_product(request):
    product_form = forms.ProductCreationForm()

    if request.method == "POST":
        product_form = forms.ProductCreationForm(request.POST)
        if product_form.is_valid():
            response = product_form.create_product()
            if response["errors"]:
                messages.add_message(
                    request,
                    messages.ERROR,
                    "Error in creating new product.")
            else:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Product Created Successfully.")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Error in creating new product. Please enter valid data.")

    kwargs = locals()
    return render(request, 'inventory/create_product.html', kwargs)


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
