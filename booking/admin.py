from django.contrib import admin, messages
from .models import Table, Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'date', 'start_time', 'party_size', 'table', 'status', 'created_at']
    actions = ['confirm_selected_bookings', 'reject_selected_bookings']

    def confirm_selected_bookings(self, request, queryset):
        for booking in queryset:
            if booking.status == 'Pending':
                booking.confirm_booking()

    confirm_selected_bookings.short_description = "Confirm selected bookings"

    def reject_selected_bookings(self, request, queryset):
        queryset.update(status='Rejected')

    reject_selected_bookings.short_description = "Reject selected bookings"

admin.site.register(Table)
admin.site.register(Booking, BookingAdmin)