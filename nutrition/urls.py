from django.urls import path
from . import views

urlpatterns = [
    path('', views.NutritionApiLanding.as_view(), name='nutrition-api-landing'),
    path("plans/", views.DietPlanListCreate.as_view(), name="dietplan-list"),
    path("plans/<int:pk>/", views.DietPlanDetail.as_view(), name="dietplan-detail"),
    path("meals/", views.MealListCreate.as_view(), name="meal-list"),
    path("meals/<int:pk>/", views.MealDetail.as_view(), name="meal-detail"),
]
