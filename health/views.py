from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import HealthLog
from .serializers import HealthLogSerializer

# View for listing and creating health logs
# This view allows users to retrieve their health logs or create a new log entry.
# Users can filter their logs by date.
# The user must be authenticated to access this view.
# Authentication is handled by the REST framework's JWT authentication.
from rest_framework.permissions import IsAuthenticated

class HealthLogListCreate(generics.ListCreateAPIView):
    serializer_class = HealthLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["date"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HealthLog.objects.filter(user=self.request.user)

# health log details
class HealthLogDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HealthLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HealthLog.objects.filter(user=self.request.user)
