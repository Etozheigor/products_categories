# Generated by Django 4.2.4 on 2023-08-29 10:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_productcategory_product_categories_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Товар", "verbose_name_plural": "Товары"},
        ),
        migrations.AlterModelOptions(
            name="productcategory",
            options={
                "verbose_name": "Категория товара",
                "verbose_name_plural": "Категории товаров",
            },
        ),
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
    ]
