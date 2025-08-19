from django.urls import path
from . import views

urlpatterns = [
    path("plans/", views.WorkoutPlanListCreate.as_view(), name="plan-list"),
    path("plans/<int:pk>/", views.WorkoutPlanDetail.as_view(), name="plan-detail"),
    path("exercises/", views.ExerciseListCreate.as_view(), name="exercise-list"),
    path("exercises/<int:pk>/", views.ExerciseDetail.as_view(), name="exercise-detail"),
    path("progress/", views.ProgressLogListCreate.as_view(), name="progress-list"),
    path("progress/<int:pk>/", views.ProgressLogDetail.as_view(), name="progress-detail"),
]

