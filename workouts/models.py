from django.db import models
from django.conf import settings


# workout plan model to manage workout routines and exercises
class WorkoutPlan(models.Model):
    class Level(models.TextChoices):
        BEGINNER = "beginner", "Beginner"
        INTERMEDIATE = "intermediate", "Intermediate"
        ADVANCED = "advanced", "Advanced"

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    level = models.CharField(max_length=20, choices=Level.choices, default=Level.BEGINNER)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="plans")
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# exercise model for managing exercises within a workout plan and tracking the progress
class Exercise(models.Model):
    plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name="exercises")
    name = models.CharField(max_length=150)
    sets = models.PositiveIntegerField(default=3)
    reps = models.PositiveIntegerField(default=10)
    rest_seconds = models.PositiveIntegerField(default=60)
    video_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.plan.title})"

# progress log model for tracking user progress on exercises
class ProgressLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="progress_logs")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="logs")
    date = models.DateField()
    sets_done = models.PositiveIntegerField(default=0)
    reps_done = models.PositiveIntegerField(default=0)
    notes = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ("user", "exercise", "date")
        ordering = ["-date"]
