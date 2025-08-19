from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import DietPlan, Meal
from .serializers import DietPlanSerializer, MealSerializer
from .permissions import IsTrainerOrNutritionistOrReadOnly

# Views for managing diet plans and meals
# create DietPlan list views
class DietPlanListCreate(generics.ListCreateAPIView):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer
    permission_classes = [IsTrainerOrNutritionistOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["goal_type", "is_public"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "title"]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# DietPlan detail view
class DietPlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer
    permission_classes = [IsTrainerOrNutritionistOrReadOnly]

# Meal list and create view
# Allows trainers and nutritionists to create meals within a diet plan
class MealListCreate(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsTrainerOrNutritionistOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["diet_plan"]

# Meal detail view
# Allows trainers and nutritionists to update and delete meals within a diet plan
class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsTrainerOrNutritionistOrReadOnly]
