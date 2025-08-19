from rest_framework import serializers
from .models import DietPlan, Meal

# Serializer for Meal model
# Used for validating and serializing meal data
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ["id", "diet_plan", "name", "calories", "protein_g", "carbs_g", "fat_g"]

# Serializer for DietPlan model
# Used for validating and serializing diet plan data
class DietPlanSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True, read_only=True)
    created_by_username = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = DietPlan
        fields = ["id", "title", "description", "goal_type", "is_public", "created_by",
                  "created_by_username", "meals", "created_at"]
        read_only_fields = ["created_by", "created_by_username", "created_at"]

    def create(self, validated_data):
        user = self.context["request"].user
        return DietPlan.objects.create(created_by=user, **validated_data)
