from rest_framework import serializers
from .models import HealthLog

# Serializer for HealthLog model
# This serializer handles the validation and creation of health log entries
class HealthLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthLog
        fields = ["id", "user", "date", "weight_kg", "bmi", "bp_systolic", "bp_diastolic", "sleep_hours", "water_ml"]
        read_only_fields = ["user"]

    def validate(self, attrs):
        # Auto-calc BMI if not provided
        
        if not attrs.get("bmi") and attrs.get("weight_kg") and self.context["request"].user.height_cm:
            height_m = self.context["request"].user.height_cm / 100
            attrs["bmi"] = round(attrs["weight_kg"] / (height_m ** 2), 2)
        return attrs

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
