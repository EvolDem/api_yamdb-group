from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_admin
        if request.method in SAFE_METHODS:
            return True
        return False


class IsAuthorModeratorAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or request.user == obj.author
                or request.user.is_moderator
                or request.user.is_admin)


class IsAdminStaffOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_admin
                or request.user.is_staff)
