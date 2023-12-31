# Generated by Django 4.2.4 on 2023-08-28 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, unique=True, verbose_name="Имя"),
                ),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="Описание"),
                ),
                ("price", models.FloatField(verbose_name="Цена")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="products_images",
                        verbose_name="Картинка",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False, verbose_name="Опубликован ли товар"
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="Удален ли товар"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="products.category",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория продукта",
                "verbose_name_plural": "Категори продуктов",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="categories",
            field=models.ManyToManyField(
                related_name="products",
                through="products.ProductCategory",
                to="products.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AddConstraint(
            model_name="productcategory",
            constraint=models.UniqueConstraint(
                fields=("product", "category"), name="unique_product_category"
            ),
        ),
    ]
