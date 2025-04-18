from rest_framework import serializers # serializers are use to convert data to JSON format
from .models import Menu, Booking
from django.contrib.auth.models import User  # Import User model for authentication


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'  # Serialize all fields of the Menu model
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # Serialize all fields of the Booking model
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']  # Serialize specific fields of the User model