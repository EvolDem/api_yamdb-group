from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or request.user.is_admin
                or request.user.is_staff)


class IsAuthorModeratorAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or request.user == obj.author
                or request.user.is_moderator
                or request.user.is_admin
                or request.user.is_staff)


class IsAdminStaff(BasePermission):
    def has_permission(self, request, view, obj):
        return request.user.is_admin or request.user.is_staff
