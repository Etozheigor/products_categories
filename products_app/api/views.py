from rest_framework import viewsets

from products.models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для категорий."""

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
