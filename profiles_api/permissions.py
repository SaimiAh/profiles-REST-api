from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermissiond):
    """Allow User to edit his own profile."""
    def has_object_permission(self, request, view, obj)
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
