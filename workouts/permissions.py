from rest_framework.permissions import BasePermission, SAFE_METHODS

# this file for the custom permissions so user[trainer and admin] can manage their workout plans and progress
# to ensure that users can only edit their own plans and logs
# Custom permission to allow only trainers and admins to edit

# Trainer or Admin can edit workout plans and progress logs
class IsTrainerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return getattr(request.user, "role", None) in ("trainer", "admin")

# Custom permission to allow only owners, trainers, and admins to edit
# exercise progress logs
class IsOwnerTrainerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return (getattr(request.user, "id", None) == getattr(obj.created_by, "id", None)
                or getattr(request.user, "role", None) == "admin")
