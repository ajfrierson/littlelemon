from django.urls import path
from .views import MenuView, BookingView, IndexView, UserViewSet



urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Home page
    path('menu/', MenuView.as_view(), name='menu'),  # Menu page
    path('booking/', BookingView.as_view(), name='bookings'),  # Bookings page
]