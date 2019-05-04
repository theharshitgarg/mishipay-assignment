from just_shoping.settings.common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', 'mos-mishipay.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1jd3jvubg4mi9',
        'USER': 'undndxuvltjkkf',
        'PASSWORD': '9c32ef58c9da8578cf521158a92fc765526975ac91f663b947a116da816cd71d',
        'HOST': 'ec2-50-19-127-115.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

SHOPIFY_SETTINGS = {
    "KEY": os.environ['SHOPIFY_KEY'],
    "PASSWORD": os.environ['SHOPIFY_PASSWORD'],
    "SHOP_URL": "ishoppersstop.myshopify.com",
}


