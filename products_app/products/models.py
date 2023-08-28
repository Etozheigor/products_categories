from django.db import models


class Category(models.Model):
    """Модель категорий."""

    name = models.CharField(verbose_name='Имя', max_length=50, unique=True)
    description = models.CharField(verbose_name='Описание', max_length=100)




