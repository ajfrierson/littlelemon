from django.contrib import admin
from .models import Booking, Menu

# Register your models here.
admin.site.register(Booking)
admin.site.register(Menu)
# Register the Booking and Menu models with the Django admin site