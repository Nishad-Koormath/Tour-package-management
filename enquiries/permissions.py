from rest_framework.permissions import BasePermission, SAFE_METHODS

class EnquiryPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return request.user and request.user.is_authenticated and request.user.is_staff
    