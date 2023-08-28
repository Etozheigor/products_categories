from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(v1_router.urls)),
    path(
        'users/',
        UserViewSet.as_view({'post': 'create'}),
        name='user-create'
    ),
    path('auth/', include('djoser.urls.jwt')),
]
