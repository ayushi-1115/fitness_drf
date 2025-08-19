from rest_framework.permissions import BasePermission, SAFE_METHODS

# permission for trainers and nutritionists
# Allows read-only access for all users, but write access only for trainers, nutritionists, and admins
class IsTrainerOrNutritionistOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return getattr(request.user, "role", None) in ("trainer", "nutritionist", "admin")
