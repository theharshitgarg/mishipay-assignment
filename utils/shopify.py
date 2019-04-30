from django.conf import settings
import requests
import json
try:
    from urllib.parse import urlparse, urljoin
except ImportError:
    from urlparse import urlparse, urljoin

ENDPOINTS = {
    "PRODUCTS": "admin/api/2019-04/products.json",
    "ORDERS": "admin/api/2019-04/orders.json",
}

def get_uri():
    url = "https://" + "{KEY}:{PASSWORD}" + "@" + settings.SHOPIFY_SETTINGS['SHOP_URL']
    url = url.format(
            KEY=settings.SHOPIFY_SETTINGS['KEY'],
            PASSWORD=settings.SHOPIFY_SETTINGS['PASSWORD']
        )

    return url


def post_request():
    pass


def get_product_request():
    url = get_uri()
    url = urljoin(url, ENDPOINTS['PRODUCTS'])

    resp = requests.get(url)
    return resp


def get_orders_request():
    url = get_uri()
    url = urljoin(url, ENDPOINTS['ORDERS'])

    resp = requests.get(url)
    return resp


def create_order(payload):
    url = get_uri()
    url = urljoin(url, ENDPOINTS['ORDERS'])
    headers = {
        'content-type': "application/json",
    }

    response = requests.request("POST", url,
                    data=json.dumps(payload),
                    headers=headers,
                )
    
    return json.loads(response.content.decode('utf-8'))
    