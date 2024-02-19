from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.db import models
from django.utils import timezone
from .models import Booking, Table

# Create your views here.
class BookingList(generic.ListView):
    template_name = "booking/index.html"
    context_object_name= "index"

    def get_queryset(self):
        return Booking.objects.all().order_by('-date')

class BookingDetail(generic.DetailView):
    model = Booking
    template_name = "booking/details.html"

class CreateBooking(generic.edit.CreateView):
    model = Booking
    fields = ['id', 'username', 'customer_name', 'date', 'start_time', 'end_time', 'party_size', 'table', 'notes', 'created_at']
    template_name = "booking/create.html"

class UpdateBooking(generic.edit.UpdateView):
    model = Booking
    fields = ['id', 'username', 'customer_name', 'date', 'start_time', 'end_time', 'party_size', 'table', 'notes', 'created_at']
    template_name = "booking/update.html"

class DeleteBooking(generic.edit.DeleteView):
    model = Booking
    success_url = reverse_lazy('reservation:index')
    template_name = "booking/delete.html"

#class HomePage(generic.TemplateView):
    #template_name="booking/index.html"