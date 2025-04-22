# littlelemon
Test the following API endpoints:
  path('', IndexView.as_view(), name='index'),  # Home page
  path('booking/', BookingView.as_view(), name='bookings'),  # Bookings page
  path('booking/<int:pk>/', SingleBookingView.as_view(), name='booking_detail'),  # Single booking page
  path('menu/', MenuItemView.as_view(), name='menu_items'),  # Menu items page
  path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu_item_detail'),  # Single menu item page