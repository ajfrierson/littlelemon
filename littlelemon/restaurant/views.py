from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer



# Create your views here.
class BookingView(APIView):
    
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data) # Return all bookings in JSON format
    
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
class MenuView(APIView):
    
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    
class IndexView(APIView):
    
    def get(self, request):
        return render(request, 'index.html')  # Render the index.html template