from django.contrib import admin
from .models import Table, Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'start_time', 'party_size', 'table', 'status']
    actions = ['confirm_selected_bookings', 'reject_selected_bookings']

    def confirm_selected_bookings(modeladmin, request, queryset):
        queryset.update(status='Confirmed')

    confirm_selected_bookings.short_description = "Confirm selected bookings"

    def reject_selected_bookings(modeladmin, request, queryset):
        queryset.update(status='Rejected')

    reject_selected_bookings.short_description = "Reject selected bookings"

admin.site.register(Table)
admin.site.register(Booking, BookingAdmin)