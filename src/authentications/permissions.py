from rest_framework import permissions
from authentications.models import ChefBook


class IsChef(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_chef)
    
    

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        chef=ChefBook.objects.get(chef=request.user)
        return obj.chef == chef