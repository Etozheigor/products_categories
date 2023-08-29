from django.contrib import admin

from .models import Category, Product, ProductCategory


class ProductCategoryInLine(admin.TabularInline):
    """Кастомный класс для отображения в админке поля категорий товаров."""

    model = ProductCategory


@admin.register(Product)
class BookmarkAdmin(admin.ModelAdmin):
    """Кастомный класс для администрирования модели продуктов."""

    inlines = (ProductCategoryInLine,)


admin.site.register(Category)
admin.site.register(ProductCategory)
