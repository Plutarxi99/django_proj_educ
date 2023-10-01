from django.core.management import BaseCommand

from catalog.models import Product, Category
from django.db import connection


class Command(BaseCommand):
    help = 'Заполнение базы данных'

    def handle(self, *args, **options):
        # Подключается к базе данных и обнуляет автоинкремент и удаляет наполнение таблиц
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM catalog_product;')
            cursor.execute('DELETE FROM catalog_category;')
            cursor.execute('TRUNCATE TABLE catalog_product RESTART IDENTITY;')
            cursor.execute('TRUNCATE TABLE catalog_category RESTART IDENTITY;')

        # Добавляет данные в таблицу catalog_product
        product_list = [
            {'name': 'ручка', 'description': 'для письма', 'pictures': 'plut.png', 'category': '1', 'price': '50'},
            {'name': 'компьютер', 'description': 'для учебы', 'category': '2', 'price': '30000'},
            {'name': 'тетрадь', 'description': 'для письма', 'category': '1', 'price': '100'},
            {'name': 'клавиатура', 'description': 'для учебы', 'category': '2', 'price': '2000'}
        ]
        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )
        Product.objects.bulk_create(product_for_create)
        # Добавляет данные в таблицу catalog_category
        category_list = [
            {'name': 'канцелярия', 'description': 'для принадлежностей письма'},
            {'name': 'школа', 'description': 'для обработки не автоматизированного кода'}
        ]
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Product(**category_item)
            )
        Category.objects.bulk_create(category_for_create)
