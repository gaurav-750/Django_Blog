from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # read-only for any requests:
        if request.method in permissions.SAFE_METHODS:  # Get, head, options
            return True

        # write permissions are only allowed to the author of the post
        return obj.author == request.user
