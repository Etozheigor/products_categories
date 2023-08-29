from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.response import Response

from products.models import Category, Product
from .filters import ProductFilter
from .permissions import IsAdminOrReadOnly
from .serializers import (CategorySerializer, ProductReadSerializer,
                          ProductWriteSerializer)


class CategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для категорий."""

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAdminOrReadOnly,)

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        if category.products.count() > 0:
            return Response(
                {
                    'error': 'Невозможно удалить объект, так как'
                    'есть продукты, относящиеся к этой категории.'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().destroy(request, *args, **kwargs)


class ProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для продуктов."""

    queryset = Product.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    filterset_fields = ('name', 'is_published', 'is_deleted')

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ProductReadSerializer
        return ProductWriteSerializer

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.is_deleted = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
