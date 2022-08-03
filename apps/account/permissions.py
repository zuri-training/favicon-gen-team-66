from rest_framework import permissions


class IsCreatorOrAdmin(permissions.BasePermission):
    # actions to change data
    edit_methods = ('PUT', 'PATCH')
    
    # permissions for specific actions
    def has_object_permission(self, request, view, obj):
        # if request is get
        if request.method in permissions.SAFE_METHODS:
            return True
        # if user making the request is a staff and not either put or patch
        if request.user_is_staff and request.method not in self.edit.methods:
            return True
        # if user making the request is a superuser
        if request.user_is_superuser:
            return True
        # if user making the request is the object owner
        if request.user == obj:
            return True