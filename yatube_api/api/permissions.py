from rest_framework import permissions


class AuthOrAuthorOrReadOnly(permissions.BasePermission):
    """
    Кастомный пермишн, который разрешает полный доступ к объекту только автору.

    В has_permission проверяем метод и авторизацию. Eсли результат: True,
    то в has_object_permission получаем доступ к объекту. Проверяем метод и
    является ли пользователь владельцем объекта.
    """

    def has_permission(self, request, view):
        # Возвращает True если метод "безопасный"
        # или пользователь авторизован.
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Возвращает True если метод "безопасный"
        # или пользователь владелец объекта.
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
