from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET" or request.method == "POST" and request.user.is_authenticated:
            return True
        return request.user == view.get_object().author or request.user.is_superuser
