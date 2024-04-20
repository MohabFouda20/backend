from algoliasearch_django import AlgoliaIndex
from .models import Product
from algoliasearch_django.decorators import register


@register(Product)
class productIndex(AlgoliaIndex):
    fields = [
        'title',
        'content',
        'price',
        'user',
        'public',
    ]