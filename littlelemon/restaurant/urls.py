from django.urls import path,include
from .views import IndexView, MenuItemView, SingleMenuItemView, BookingView, SingleBookingView, UserView
from rest_framework.authtoken.views import obtain_auth_token






urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Home page
    # path('menu/', MenuView.as_view(), name='menu'),  # Menu page
    path('booking/', BookingView.as_view(), name='bookings'),  # Bookings page
    path('booking/<int:pk>/', SingleBookingView.as_view(), name='booking_detail'),  # Single booking page
    path('menu/', MenuItemView.as_view(), name='menu_items'),  # Menu items page
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu_item_detail'),  # Single menu item page
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token authentication endpoint
    path('users/<int:pk>/', UserView.as_view(), name='user_detail'),
]
