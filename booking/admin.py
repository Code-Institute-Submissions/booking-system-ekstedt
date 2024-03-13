from django.contrib import admin, messages
from django.utils.html import format_html
from .models import Table, Booking, BookingHistory
from django.urls import reverse
from django.http import HttpResponseRedirect

# Register your models here.
class PendingBookingFilter(admin.SimpleListFilter):
    title = 'Status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return(
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('rejected', 'Rejected'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'pending':
            return queryset.filter(status='Pending')
        elif self.value() == 'confirmed':
            return queryset.filter(status='Confirmed')
        elif self.value() == 'rejected':
            return queryset.filter(status='Rejected')

class BookingAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Booking model.

    Attributes:
        list_display (list): A list of fields to display in the admin change list.
        actions (list): A list of custom actions that can be performed on selected bookings.
    """
    list_display = ['user', 'name', 'date', 'start_time', 'party_size', 'table', 'status', 'created_at', 'custom_actions']
    actions = ['confirm_selected_bookings', 'reject_selected_bookings']
    list_filter = [PendingBookingFilter]

    def custom_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Confirm</a>&nbsp;'
            '<a class="button" href="{}">Reject</a>',
            reverse('admin:confirm_booking', args=[obj.pk]),
            reverse('admin:reject_booking', args=[obj.pk])
        )

    custom_actions.allows_tags = True

    def get_urls(self):
        from django.urls import path

        urls = super().get_urls()
        custom_urls = [
            path('<path:object_id>/confirm/', self.confirm_booking, name='confirm_booking'),
            path('<path:object_id>/reject/', self.reject_booking, name='reject_booking'),
        ]
        return custom_urls + urls
    
    def confirm_booking(self, request, object_id):
        booking= self.get_object(request, object_id)
        if booking and (booking.status == 'Pending' or booking.status == 'Rejected'):
            booking.confirm_booking()

            BookingHistory.objects.create(booking=booking, action='confirmed', user=request.user)

            self.message_user(request, f'Booking for {booking.user} confirmed successfully.', messages.SUCCESS)
        else:
            self.message_user(request, f'Selected booking cannot be confirmed.', messages.ERROR)
        
        return HttpResponseRedirect(reverse('admin:booking_booking_changelist'))

    def reject_booking(self, request, object_id):
        queryset = self.get_queryset(request)
        booking = queryset.get(pk=object_id)
        booking.status = 'Rejected'
        booking.save()

        BookingHistory.objects.create(booking=booking, action='rejected', user=request.user)

        self.message_user(request, 'Selected booking rejected succesfully.', messages.SUCCESS)
        
        return HttpResponseRedirect(reverse('admin:booking_booking_changelist'))

    def confirm_selected_bookings(self, request, queryset):
        for booking in queryset:
            if booking.status == 'Pending':
                booking.confirm_booking()
        self.message_user(request, f'{len(queryset)} bookings confirmed successfully.', messages.SUCCESS)
        pass

    confirm_selected_bookings.short_description = "Confirm selected bookings"

    def reject_selected_bookings(self, request, queryset):
        queryset.filter(status='Pending').update(status='Rejected')
        self.message_user(request, f'{len(queryset)} bookings rejected successfully.', messages.SUCCESS)
        pass

    reject_selected_bookings.short_description = "Reject the selected bookings"

class BookingHistoryAdmin(admin.ModelAdmin):
    list_display = ['booking', 'action', 'timestamp', 'user']
    search_fields = ['booking__user__username', 'action']
    list_filter = ['action', 'timestamp']
    readonly_fields = ['booking', 'action', 'timestamp', 'user']

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Table)
admin.site.register(Booking, BookingAdmin)
admin.site.register(BookingHistory, BookingHistoryAdmin)