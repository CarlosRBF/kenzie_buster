from rest_framework import permissions
from .models import Movie

class MyCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False


class MyCustomPermissionTokenValid(permissions.BasePermission):
    def has_object_permission(self, request, view, movie: Movie) -> bool:
        return movie.user == request.user 
