from django.db import models


class Category(models.Model):
    """Модель категорий."""

    name = models.CharField(verbose_name='Имя', max_length=50, unique=True)
    description = models.CharField(verbose_name='Описание', max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Модель товаров."""

    name = models.CharField(verbose_name='Имя', max_length=50, unique=True)
    description = models.CharField(verbose_name='Описание', max_length=100)
    price = models.FloatField(verbose_name='Цена')
    image = models.ImageField(
        'Картинка', blank=True, null=True, upload_to='products_images'
    )
    is_published = models.BooleanField(
        verbose_name='Опубликован ли товар', default=False
    )
    is_deleted = models.BooleanField(
        verbose_name='Удален ли товар', default=False)
    categories = models.ManyToManyField(
        Category,
        through='ProductCategory',
        verbose_name='Категория',
        related_name='products',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductCategory(models.Model):
    """Промежуточная модель для связи продукт-категори."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        constraints = (
            models.UniqueConstraint(
                fields=('product', 'category'), name='unique_product_category'
            ),
        )
