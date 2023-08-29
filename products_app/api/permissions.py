from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Пермишен для доступка к продуктам и категориям.

    Чтение доступно всем пользователям.
    Редактирование доступно только для администратора.
    """

    message = 'Редактирование доступно только администратору'

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser
