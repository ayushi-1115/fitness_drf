from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User 

# user serializer for listing and retrieving the user details  and for updating the user details
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','first_name', 'last_name' , 'role', 'height_cm', 'weight_kg', 'goal']
        read_only_fields = ['id', 'role']


# register serializer for creating a new user and validating the password 
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
           model = User
           fields = ['username', 'email', 'password']


    def validate_password(self, value):
        validate_password(value)
        return value
    

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user 




