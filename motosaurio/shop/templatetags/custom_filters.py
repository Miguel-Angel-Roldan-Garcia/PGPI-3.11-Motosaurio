from shop.models import Product
from django import template

register = template.Library()

@register.filter(name='title_value')
def title_value(value):
    return value.title()

@register.filter(name='parse_producer')
def parse_producer(value):
    return Product.producers_dict[value]

@register.filter(name='parse_product_type')
def parse_product_type(value):
    return Product.type_choices_dict[value]