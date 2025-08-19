from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# create a custom user model by extending abstracting AbstractUser
# add additional fields in this class if we need to add more fields to the user model
class User(AbstractUser):
    class Role(models.TextChoices):
        USER = 'user', 'User',
        ADMIN = 'admin', 'Admin',
        NUTRITIONIST = 'nutritionist', 'Nutritionist',
        TRAINER = 'trainer', 'Trainer'
    role = models.CharField(max_length=20, choices= Role.choices, default=Role.USER)
    height_cm = models.FloatField(null=True, blank=True)
    weight_kg = models.FloatField(null=True, blank=True)
    goal = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return f"{self.username}({self.role})"

