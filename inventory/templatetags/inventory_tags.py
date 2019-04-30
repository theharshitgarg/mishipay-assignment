from django import template
import datetime

register = template.Library()

@register.filter(name='inventory_date')
def inventory_date(value):
    return '12 Jan 2019'



