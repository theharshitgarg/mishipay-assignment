# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from inventory import models

admin.site.register(models.Vendor)
admin.site.register(models.Category)
admin.site.register(models.Product)
