from django.contrib import admin
from .models import WorkoutPlan, Exercise, ProgressLog

# register the models for the admin interface 

admin.site.register(WorkoutPlan)
admin.site.register(Exercise)
admin.site.register(ProgressLog)
