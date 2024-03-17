from django.contrib import admin, messages
from django.utils.html import format_html
from .models import Table, Booking, BookingHistory
from django.urls import reverse
from django.http import HttpResponseRedirect


# Register your models here.
class PendingBookingFilter(admin.SimpleListFilter):
    """
    Custom admin filter for filtering bookings based on their status.

    title (str): The displayed title for the filter.
    parameter_name (str): The parameter name used in the URL.
    """
    title = 'Status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('rejected', 'Rejected'),)

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
        list_display (list): A list of fields
        to display in the admin change list.
        actions (list): A list of custom actions
        that can be performed on selected bookings.
    """
    list_display = ['user', 'name', 'date', 'start_time',
                    'party_size', 'table', 'status',
                    'created_at', 'custom_actions']
    actions = ['confirm_selected_bookings', 'reject_selected_bookings']
    list_filter = [PendingBookingFilter]

    def custom_actions(self, obj):
        """
        Custom method to display HTML links for confirming
        and rejecting bookings in the admin change list.

        Args:
            obj: The booking object.

        Returns:
            str: HTML-formatted links for confirming and rejecting bookings.
        """
        return format_html(
            '<a class="button" href="{}">Confirm</a>&nbsp;'
            '<a class="button" href="{}">Reject</a>',
            reverse('admin:confirm_booking', args=[obj.pk]),
            reverse('admin:reject_booking', args=[obj.pk])
        )

    custom_actions.allows_tags = True

    def get_urls(self):
        """
        Custom method to extend the default admin
        URLs with confirm and reject booking URLs.

        Returns:
            list: List of custom URL patterns.
        """
        from django.urls import path

        urls = super().get_urls()
        custom_urls = [
            path(
                '<path:object_id>/confirm/',
                self.confirm_booking,
                name='confirm_booking'),
            path(
                '<path:object_id>/reject/',
                self.reject_booking, name='reject_booking'),
        ]
        return custom_urls + urls

    def confirm_booking(self, request, object_id):
        """
        Custom method for confirming a booking in the admin interface.

        Args:
            request: The HTTP request object.
            object_id (str): The ID of the booking to be confirmed.

        Returns:
            HttpResponseRedirect: Redirects
            to the booking change list page after confirming the booking.
        """
        booking = self.get_object(request, object_id)
        if booking and (
                booking.status == 'Pending' or booking.status == 'Rejected'):
            booking.confirm_booking()

            BookingHistory.objects.create(
                booking=booking, action='confirmed', user=request.user)

            self.message_user(
                request,
                f'Booking for {booking.user} confirmed successfully.',
                messages.SUCCESS)
        else:
            self.message_user(
                request,
                f'Selected booking cannot be confirmed.',
                messages.ERROR)

        return HttpResponseRedirect(
                reverse('admin:booking_booking_changelist'))

    def reject_booking(self, request, object_id):
        """
        Custom method for rejecting a booking in the admin interface.

        Args:
            request: The HTTP request object.
            object_id (str): The ID of the booking to be rejected.

        Returns:
            HttpResponseRedirect: Redirects to the
            booking change list page after rejecting the booking.
        """
        queryset = self.get_queryset(request)
        booking = queryset.get(pk=object_id)
        booking.status = 'Rejected'
        booking.save()

        BookingHistory.objects.create(
            booking=booking, action='rejected', user=request.user)

        self.message_user(
                        request,
                        'Selected booking rejected succesfully.',
                        messages.SUCCESS)

        return HttpResponseRedirect(
                reverse('admin:booking_booking_changelist'))

    def confirm_selected_bookings(self, request, queryset):
        """
        Custom admin action to confirm multiple selected bookings.

        Args:
            request: The HTTP request object.
            queryset: The selected Booking objects to be confirmed.

        Returns:
            None
        """
        for booking in queryset:
            if booking.status == 'Pending':
                booking.confirm_booking()
        self.message_user(
            request,
            f'{len(queryset)} bookings confirmed successfully.',
            messages.SUCCESS)
        pass

    confirm_selected_bookings.short_description = "Confirm selected bookings"

    def reject_selected_bookings(self, request, queryset):
        """
        Custom admin action to reject multiple selected bookings.

        Args:
            request: The HTTP request object.
            queryset: The selected Booking objects to be rejected.

        Returns:
            None
        """
        queryset.filter(status='Pending').update(status='Rejected')
        self.message_user(
            request,
            f'{len(queryset)} bookings rejected successfully.',
            messages.SUCCESS)
        pass

    reject_selected_bookings.short_description = "Reject the selected bookings"


class BookingHistoryAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the BookingHistory model.

    list_display (list):
    A list of fields to display in the admin change list.
    search_fields (list):
    A list of fields to enable searching in the admin interface.
    list_filter (list):
    A list of fields to enable filtering in the admin interface.
    readonly_fields (list):
    A list of fields that are read-only in the admin interface.

    """
    list_display = ['booking', 'action', 'timestamp', 'user']
    search_fields = ['booking__user__username', 'action']
    list_filter = ['action', 'timestamp']
    readonly_fields = ['booking', 'action', 'timestamp', 'user']

    def has_change_permission(self, request, obj=None):
        """
        Custom method to restrict the change
        permission for BookingHistory objects.

        Args:
            request: The HTTP request object.
            obj: The BookingHistory object.

        Returns:
            bool: whether the user has change permission.
        """
        return False


admin.site.register(Table)
admin.site.register(Booking, BookingAdmin)
admin.site.register(BookingHistory, BookingHistoryAdmin)
