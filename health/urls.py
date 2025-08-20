from django.urls import path
from . import views

urlpatterns = [
    path('', views.HealthApiLanding.as_view(), name='health-api-landing'),
    path("logs/", views.HealthLogListCreate.as_view(), name="healthlog-list"),
    path("logs/<int:pk>/", views.HealthLogDetail.as_view(), name="healthlog-detail"),
]
