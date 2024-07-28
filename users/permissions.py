from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    """Проверка на модератора"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Модераторы").exists()


class IsOwner(BasePermission):
    """Проверка на владельца объекта"""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class IsOwnerProfile(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.oid == request.user.id:
            return True
        return False

