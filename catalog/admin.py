from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # fields = ('pk', 'name',)
    list_display = ('pk', 'name', 'price', 'category',)
    search_fields = ('name', 'description',)
    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'version_number', 'version_name', 'version_is_active',)





