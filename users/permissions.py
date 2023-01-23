from rest_framework import permissions
from .models import User

class MyCustomPermissionTokenValid(permissions.BasePermission):
    def has_object_permission(self, request, view, user: User) -> bool:
        if request.user.is_superuser:
            return True

        if user.id == request.user.id:
            return True

        return False
