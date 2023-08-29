import django_filters
from products.models import Product


class ProductFilter(django_filters.FilterSet):
    """Фильтр для модели продуктов."""

    price_gte = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte'
    )
    price_lte = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte'
    )
    categories = django_filters.CharFilter(field_name='categories__name')

    class Meta:
        model = Product
        fields = [
            'price_gte',
            'price_lte',
            'name',
            'is_published',
            'is_deleted',
            'categories'
        ]
