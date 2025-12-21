from rest_framework.permissions import BasePermission

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Client").exists()
    
class IsSupportOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(
            name__in = ["Support","Admin"]
            ).exists()
    
class IsDeveloper(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Developer").exists()