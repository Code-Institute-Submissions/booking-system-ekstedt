from django.contrib import admin, messages
from .models import Table, Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Booking model.

    Attributes:
        list_display (list): A list of fields to display in the admin change list.
        actions (list): A list of custom actions that can be performed on selected bookings.
    """
    list_display = ['user', 'name', 'date', 'start_time', 'party_size', 'table', 'status', 'created_at']
    actions = ['confirm_selected_bookings', 'reject_selected_bookings']

    def confirm_selected_bookings(self, request, queryset):
        """
        Action method to confirm selected bookings.

        Parameters:
            request (HttpRequest): The current HTTP request.
            queryset (QuerySet): The selected bookings to be confirmed.

        Returns:
            None
        """
        for booking in queryset:
            if booking.status == 'Pending':
                booking.confirm_booking()

    confirm_selected_bookings.short_description = "Confirm selected bookings"

    def reject_selected_bookings(self, request, queryset):
        """
        Action method to reject selected bookings.

        Parameters:
            request (HttpRequest): The current HTTP request.
            queryset (QuerySet): The selected bookings to be rejected.

        Returns:
            None
        """
        queryset.update(status='Rejected')

    reject_selected_bookings.short_description = "Reject selected bookings"

admin.site.register(Table)
admin.site.register(Booking, BookingAdmin)