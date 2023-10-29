from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def cache_category():

    key = 'category_list'
    category_list = cache.get(key)
    if category_list is None:
        category_list = Category.objects.all()
        cache.set(key, category_list)
        return category_list
    return category_list
