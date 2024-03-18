from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, \
    HttpResponseRedirect, Http404, \
    HttpResponseNotFound, HttpResponseServerError
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.db import models
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .models import Booking, Table
from .forms import BookingForm
from datetime import date
from .messages import (
    BOOKING_SUCCESSFUL_CREATE,
    BOOKING_SUCCESSFUL_UPDATE,
    BOOKING_SUCCESSFUL_DELETE,
)
from django.contrib import messages
from django.utils import formats


class HomePage(generic.TemplateView):
    """
    Display the home page.
    """
    template_name = "index.html"
    context_object_name = "homepage"


class MenuPage(generic.TemplateView):
    """
    Display the menu page.
    """
    template_name = "menu.html"
    context_object_name = "menu"


class HistoryPage(generic.TemplateView):
    """
    Display the history page.
    """
    template_name = "history.html"
    context_object_name = "history"


class ContactPage(generic.TemplateView):
    """
    Display the contact page.
    """
    template_name = "contact.html"
    context_object_name = "contact"


class BookingList(LoginRequiredMixin, generic.ListView):
    """
    Display a list of bookings for staff or users.
    """
    template_name = "bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        """
        Get the queryset of bookings based on user type.
        """
        if self.request.user.is_staff:
            return Booking.objects.all().order_by('-date')
        else:
            return Booking.objects.filter(
                user=self.request.user).order_by('-date')

    def get_context_data(self, **kwargs):
        """
        Add today's date and user messages to the context.
        """
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()

        user_messages = messages.get_messages(self.request)
        context['user_messages'] = user_messages
        confirmed_bookings = Booking.objects.filter(
            user=self.request.user,
            status='Confirmed',
            date__gte=timezone.now().date()
        )

        for booking in confirmed_bookings:
            formatted_date = formats.date_format(
                booking.date, format='SHORT_DATE_FORMAT')
            formatted_time = formats.time_format(
                booking.start_time, format='TIME_FORMAT')

            confirmation_message = f"Your booking for \
            {formatted_date} at {formatted_time} has been confirmed!"

            messages.success(self.request, confirmation_message)

        rejected_bookings = Booking.objects.filter(
            user=self.request.user,
            status='Rejected',
            date__gte=timezone.now().date()
        )

        for booking in rejected_bookings:
            formatted_date = formats.date_format(
                booking.date, format='SHORT_DATE_FORMAT')
            formatted_time = formats.time_format(
                booking.start_time, format='TIME_FORMAT')

            rejection_message = f"Your booking for \
                {formatted_date} at \
                    {formatted_time} has been rejected by the admin."

            messages.warning(self.request, rejection_message)

        return context


class BookingDetail(generic.DetailView):
    """
    Display details of a booking.
    """
    model = Booking
    template_name = "details.html"


@method_decorator(login_required, name='dispatch')
class Profile(generic.DetailView):
    """
    Display the user's profile with past bookings.
    """
    model = User
    template_name = "profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        """
        Get the user object.
        """
        return self.request.user

    def get_context_data(self, **kwargs):
        """
        Add past bookings to the context.
        """
        context = super().get_context_data(**kwargs)
        past_bookings = Booking.objects.filter(
            user=self.request.user,
            date__lt=timezone.now().date()
        ).order_by('-date')

        context['past_bookings'] = past_bookings

        return context


class CreateBooking(generic.edit.CreateView):
    """
    Allow users to create a new booking.
    """
    model = Booking
    form_class = BookingForm
    template_name = "create.html"
    success_url = reverse_lazy('booking:bookings')

    def get_form(self, form_class=None):
        """
        Set the request attribute in the form.
        """
        form = super().get_form(form_class)
        form.request = self.request
        return form

    def form_valid(self, form):
        """
        Validate the form and create a new booking.
        """
        form.instance.user = self.request.user

        if not self.request.user.is_staff:
            today = timezone.now().date()
            if form.instance.date <= today:
                form.add_error(
                    'date', 'Tables can only be booked for future dates.')
        response = super().form_valid(form)

        messages.success(self.request, BOOKING_SUCCESSFUL_CREATE)

        return response


class UpdateBooking(generic.edit.UpdateView):
    """
    Allow users to update an existing booking.
    """
    model = Booking
    form_class = BookingForm
    template_name = "update.html"
    success_url = reverse_lazy('booking:bookings')

    def get_form(self, form_class=None):
        """
        Set the request attribute in the form.
        """
        form = super().get_form(form_class)
        form.request = self.request
        return form

    def form_valid(self, form):
        """
        Validate the form and update the booking.
        """
        response = super().form_valid(form)

        messages.success(self.request, BOOKING_SUCCESSFUL_UPDATE)

        return response


class DeleteBooking(generic.edit.DeleteView):
    """
    Allow users to delete an existing booking.
    """
    model = Booking
    success_url = reverse_lazy('booking:bookings')
    template_name = "delete.html"

    def form_valid(self, form):
        """
        Delete the booking and show success message.
        """
        messages.success(self.request, BOOKING_SUCCESSFUL_DELETE)
        return super().form_valid(form)
