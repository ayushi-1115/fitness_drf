from rest_framework import serializers
from .models import WorkoutPlan, Exercise, ProgressLog


# Exercise serializer for managing exercises within a workout plan and tracking user progress
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["id", "plan", "name", "sets", "reps", "rest_seconds", "video_url"]

# Workout plan serializer for managing workout plans and their exercises for users
class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)
    created_by_username = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = WorkoutPlan
        fields = ["id", "title", "description", "level", "is_public",
                  "created_by", "created_by_username", "exercises",
                  "created_at", "updated_at"]
        read_only_fields = ["created_by", "created_by_username", "created_at", "updated_at"]

    def create(self, validated_data):
        user = self.context["request"].user
        return WorkoutPlan.objects.create(created_by=user, **validated_data)

# Progress log serializer for tracking user progress on exercises
class ProgressLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressLog
        fields = ["id", "user", "exercise", "date", "sets_done", "reps_done", "notes"]
        read_only_fields = ["user"]

    def validate(self, attrs):
        if attrs.get("sets_done", 0) > 50 or attrs.get("reps_done", 0) > 1000:
            raise serializers.ValidationError("Values look unrealistic. Please check.")
        return attrs

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
