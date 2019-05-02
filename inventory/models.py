# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

    @property
    def json(self):
        return {
            "name": self.name,
        }


class Category(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

    @property
    def json(self):
        return {
            "name": self.name,
        }


class Product(models.Model):
    name = models.CharField(max_length=400)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str_(self):
        return self.name

    @property
    def json(self):
        return {
            "name": self.name,
            "vendor": self.vendor.json,
            "category": self.category.json,
        }


class PersonQuerySet(models.QuerySet):
    def authors(self):
        return self.filter(role='A')

    def editors(self):
        return self.filter(role='E')

class PersonManager(models.Manager):
    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)

    def authors(self):
        return self.get_queryset().authors()

    def editors(self):
        return self.get_queryset().editors()

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1)
    people = PersonManager()