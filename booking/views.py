from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.db import models
from django.utils import timezone
from .models import Booking, Table
from .forms import BookingForm

# Create your views here.
class BookingList(generic.ListView):
    template_name = "index.html"
    context_object_name= "index"

    def get_queryset(self):
        return Booking.objects.all().order_by('-date')

class BookingDetail(generic.DetailView):
    model = Booking
    template_name = "details.html"

class CreateBooking(generic.edit.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "create.html"
    success_url = reverse_lazy('booking:home')

class UpdateBooking(generic.edit.UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "update.html"
    success_url = reverse_lazy('booking:home')


class DeleteBooking(generic.edit.DeleteView):
    model = Booking
    success_url = reverse_lazy('reservation:index')
    template_name = "delete.html"

#class HomePage(generic.TemplateView):
    #template_name="booking/index.html"