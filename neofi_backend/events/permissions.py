from rest_framework.permissions import BasePermission
from .models import EventPermission

class IsOwnerOrEditor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return EventPermission.objects.filter(event=obj, user=request.user, role__in=['owner', 'editor']).exists()