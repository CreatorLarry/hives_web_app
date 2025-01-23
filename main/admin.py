from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name','county', 'town', 'specifications', 'event_date', 'contact_number', 'email', 'created_at', 'num_people')
    search_fields = ('client_name','county', 'town', 'place_name', 'specifications')
    list_filter = ('event_date', 'specifications')
