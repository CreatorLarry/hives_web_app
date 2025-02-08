from django.contrib import admin
from .models import Booking, OrderableItem, Order


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'county', 'town', 'specifications', 'event_date', 'contact_number', 'email', 'created_at', 'num_people')
    search_fields = ('client_name', 'county', 'town', 'place_name', 'specifications')
    list_filter = ('event_date', 'specifications')


@admin.register(OrderableItem)
class OrderableItemAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Custom method to display the related items
    def display_items(self, obj):
        return ", ".join([item.name for item in obj.items.all()])
    display_items.short_description = 'Ordered Items'

    # Configuring the list_display
    list_display = ['client_name', 'county', 'town', 'place_name', 'specifications', 'contact_number', 'display_items']

    # Optional: You can add search fields for easier searching in the admin
    search_fields = ['client_name', 'county', 'town']
