from rest_framework import permissions

class IsMerchantOrReadOnly(permissions.BasePermission):
    message="operation not allowed"
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.user.user_role =='merchant' or (request.user.is_superuser and request.method!='POST') or (request.user.user_role=='farmer' and request.method=='PUT'):
            return True
        return False

class IsFarmerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.user.user_role =='farmer' or request.user.is_superuser:
            return True
        return False

