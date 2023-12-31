# Generated by Django 4.2.5 on 2023-10-24 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_version_only_one_active_version_for_product_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='product',
            constraint=models.CheckConstraint(check=models.Q(('price__gte', 100), ('price__isnull', True), _connector='OR'), name='price_gte_100', violation_error_message='Цена должна быть выше 100 рублей'),
        ),
    ]
