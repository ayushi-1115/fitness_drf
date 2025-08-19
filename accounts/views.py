from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User 
from .serializers import UserSerializer, RegisterSerializer

# Create your views here.

# Registerview for handling user registration 
class RegisterView(generics.CreateAPIView):
    # handle the user registrations via post request 
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]



# health check view to check if the server is running
class HealthCheckView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({"status": "ok", "message": "Server is running"})
    


# Meview for retrieving the current user's details
class Meview(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user