from django import forms
from django.forms import DateInput
from .models import Booking

class BookingForm (forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['username', 'customer_name', 'customer_email', 'date', 'start_time', 'end_time', 'party_size', 'table', 'notes']
        exclude = ['created_at']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }