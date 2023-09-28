from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование', db_comment='поле для названия продукта', unique=True)
    description = models.TextField(verbose_name='Описание')
    pictures = models.ImageField(upload_to='pictures_prod/', verbose_name='Изображение(превью)', **NULLABLE)
    category = models.IntegerField(verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    data_of_creation = models.DateTimeField(default='2018-11-20T15:58:44.767594-06:00', verbose_name='дата создания')
    data_end_change = models.DateTimeField(auto_now_add=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}/{self.data_of_creation} - {self.data_end_change}: {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование', unique=True)
    description = models.TextField(verbose_name='Описание')

    # created_at = models.DateTimeField(**NULLABLE)
    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
