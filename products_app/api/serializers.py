from rest_framework import serializers

from products.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели категорий."""

    class Meta:
        model = Category
        fields = ("name", "description")


class ProductReadSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продуктов."""

    categories_id = serializers.SerializerMethodField()
    categories_names = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price",
            "is_published",
            "is_deleted",
            "categories_id",
            "categories_names",
        )

    def get_categories_id(self, obj):
        return [category.id for category in obj.categories.all()]

    def get_categories_names(self, obj):
        return [category.name for category in obj.categories.all()]


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

    def validate(self, data):
        if data.get('categories'):
            if not 1 < len(data['categories']) < 11:
                raise serializers.ValidationError(
                    'У продукта должно быть от 2 до 10 категорий')
        return data

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
