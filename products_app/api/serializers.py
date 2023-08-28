from rest_framework import serializers

from products.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели категорий."""

    class Meta:
        model = Category
        fields = ('name', 'description')
