from django.db import models
from django.conf import settings

# Model for tracking user health metrics
# This model allows users to log their health data over time
# Users can track various health parameters such as weight, BMI, blood pressure, sleep hours, and water intake.
# The data can be used for personal insights or shared with healthcare providers.
class HealthLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="health_logs")
    date = models.DateField()
    weight_kg = models.FloatField(null=True, blank=True)
    bmi = models.FloatField(null=True, blank=True)
    bp_systolic = models.PositiveIntegerField(null=True, blank=True)
    bp_diastolic = models.PositiveIntegerField(null=True, blank=True)
    sleep_hours = models.FloatField(null=True, blank=True)
    water_ml = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "date")
        ordering = ["-date"]

    def __str__(self):
        return f"{self.user.username} - {self.date}"
