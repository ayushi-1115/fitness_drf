from django.urls import path
from . import views
from . import views_web

urlpatterns = [
    # Template-based CRUD for WorkoutPlan (trainer only)
    path("plans/web/", views_web.WorkoutPlanListView.as_view(), name="plan-list"),
    path("plans/web/create/", views_web.WorkoutPlanCreateView.as_view(), name="plan-create"),
    path("plans/web/<int:pk>/", views_web.WorkoutPlanDetailView.as_view(), name="plan-detail"),
    path("plans/web/<int:pk>/update/", views_web.WorkoutPlanUpdateView.as_view(), name="plan-update"),
    path("plans/web/<int:pk>/delete/", views_web.WorkoutPlanDeleteView.as_view(), name="plan-delete"),
    # REST API endpoints
    path("plans/", views.WorkoutPlanListCreate.as_view(), name="plan-list-api"),
    path("plans/<int:pk>/", views.WorkoutPlanDetail.as_view(), name="plan-detail-api"),
    path("exercises/", views.ExerciseListCreate.as_view(), name="exercise-list"),
    path("exercises/<int:pk>/", views.ExerciseDetail.as_view(), name="exercise-detail"),
    path("progress/", views.ProgressLogListCreate.as_view(), name="progress-list"),
    path("progress/<int:pk>/", views.ProgressLogDetail.as_view(), name="progress-detail"),
]

