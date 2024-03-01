from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.db import models
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking, Table
from .forms import BookingForm
from datetime import date

# Create your views here.
class HomePage(generic.TemplateView):
    template_name = "index.html"
    context_object_name = "homepage"

class MenuPage(generic.TemplateView):
    template_name = "menu.html"
    context_object_name = "menu"

class HistoryPage(generic.TemplateView):
    template_name = "history.html"
    context_object_name = "history"

class ContactPage(generic.TemplateView):
    template_name = "contact.html"
    context_object_name = "contact"

class BookingList(LoginRequiredMixin, generic.ListView):
    template_name = "bookings.html"
    context_object_name= "bookings"

    def get_queryset(self):
        if self.request.user.is_staff:
            return Booking.objects.all().order_by('-date')
        else:
            return Booking.objects.filter(username=self.request.user).order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        return context


class BookingDetail(generic.DetailView):
    model = Booking
    template_name = "details.html"

class CreateBooking(generic.edit.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "create.html"
    success_url = reverse_lazy('booking:bookings')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.request = self.request
        return form

    def form_valid(self, form):
        form.instance.username = self.request.user

        if not self.request.user.is_staff:
            today = timezone.now().date()
            if form.instance.date <= today:
                form.add_error('date', 'Tables can only be booked for future dates.')

        return super().form_valid(form)

class UpdateBooking(generic.edit.UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "update.html"
    success_url = reverse_lazy('booking:bookings')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.request = self.request
        return form

class DeleteBooking(generic.edit.DeleteView):
    model = Booking
    success_url = reverse_lazy('booking:bookings')
    template_name = "delete_booking.html"
