from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import WorkoutPlan, Exercise, ProgressLog
from .serializers import WorkoutPlanSerializer, ExerciseSerializer, ProgressLogSerializer
from .permissions import IsTrainerOrReadOnly, IsOwnerTrainerOrReadOnly

# WorkoutPlan views for managing workout plans and exercises

# create list of workout plans
class WorkoutPlanListCreate(generics.ListCreateAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsTrainerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["level", "is_public"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "title"]

# workout plan detail view
class WorkoutPlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsOwnerTrainerOrReadOnly]

# create execise list view
class ExerciseListCreate(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsTrainerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["plan"]

# exercise details view
class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsTrainerOrReadOnly]

# progress log list view
class ProgressLogListCreate(generics.ListCreateAPIView):
    serializer_class = ProgressLogSerializer
    def get_queryset(self):
        return ProgressLog.objects.filter(user=self.request.user)

# progress log detail view
class ProgressLogDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProgressLogSerializer
    def get_queryset(self):
        return ProgressLog.objects.filter(user=self.request.user)
