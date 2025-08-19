from django.db import models
from django.conf import settings


# Diet plan model for nutrition tracking 
class DietPlan(models.Model):
    class GoalType(models.TextChoices):
        WEIGHT_LOSS = "weight_loss", "Weight Loss"
        MUSCLE_GAIN = "muscle_gain", "Muscle Gain"
        MAINTENANCE = "maintenance", "Maintenance"

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    goal_type = models.CharField(max_length=20, choices=GoalType.choices, default=GoalType.MAINTENANCE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="diet_plans")
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.goal_type})"

# meal model for nutrition tracking 
class Meal(models.Model):
    diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE, related_name="meals")
    name = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()
    protein_g = models.FloatField(default=0)
    carbs_g = models.FloatField(default=0)
    fat_g = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} ({self.diet_plan.title})"
