from django import template
from django.db.models import Avg

from product_present.models import HandProduct


register = template.Library()


@register.filter(is_safe=True)
def comma_seperator(value):
    return '{:,}'.format(value)


@register.simple_tag
def product_rate(data):
    product = HandProduct.objects.get(id=data)
    rate = product.comment.all().aggregate(product_rate=Avg('rate'))
    return rate['product_rate']

