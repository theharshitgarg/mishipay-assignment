from just_shoping.settings.common import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1jd3jvubg4mi9',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SHOPIFY_SETTINGS = {
    "KEY": os.environ['SHOPIFY_KEY']
    "PASSWORD": os.environ['SHOPIFY_PASSWORD']
    "SHOP_URL": "ishoppersstop.myshopify.com",
}