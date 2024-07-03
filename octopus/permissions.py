from rest_framework import permissions

# ! Creating a custom permission for IsAdminOrReadOnly 

class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        
        # Allow safe methods 
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Will only return if request user is admin.
        return request.user and request.user.is_staff