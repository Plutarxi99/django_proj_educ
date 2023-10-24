from django.db import models
from django.db.models import Q

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование', db_comment='поле для названия продукта',
                            unique=True)
    description = models.TextField(verbose_name='Описание')
    pictures = models.ImageField(upload_to='pictures_prod/', verbose_name='Изображение(превью)', **NULLABLE)
    category = models.IntegerField(verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    data_of_creation = models.DateTimeField(default='2018-11-20T15:58:44.767594-06:00', verbose_name='дата создания')
    data_end_change = models.DateTimeField(auto_now_add=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}/{self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        constraints = [
            models.CheckConstraint(
                check=Q(price__gte=100) | Q(price__isnull=True),
                name="price_gte_100",
                violation_error_message='Цена должна быть выше 100 рублей'
            ),
        ]


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование', unique=True)
    description = models.TextField(verbose_name='Описание')

    # created_at = models.DateTimeField(**NULLABLE)
    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Version(models.Model):
    product_name = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.PositiveIntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=250, verbose_name='название версии')
    version_is_active = models.BooleanField(verbose_name='Активность')

    def __str__(self):
        return f'{self.product_name}/{self.version_name} - {self.version_number}: {self.version_is_active}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        constraints = [
            models.UniqueConstraint(
                fields=['product_name'],
                condition=Q(version_is_active=True),
                name='only_one_active_version_for_product',
                violation_error_message='Выберите одну активную версию'
            ),
        ]
