from rest_framework import serializers

from products.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели категорий."""

    class Meta:
        model = Category
        fields = ("name", "description")


class ProductReadSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продуктов."""

    category_id = serializers.ReadOnlyField(source="category.id")
    category_name = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price",
            "is_published",
            "is_deleted",
            "category_id",
            "category_name",
        )


class ProductWriteSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price",
            "categories",
        )

    def create(self, validated_data):
        categories = validated_data.pop("categories")
        product = Product.objects.create(**validated_data)
        product.categories.set(categories)
        product.save()
        return product

    def update(self, instance, validated_data):
        if validated_data.get("categories"):
            categories = validated_data.pop("categories")
            instance.categories.set(categories)
        return super().update(instance, validated_data)
