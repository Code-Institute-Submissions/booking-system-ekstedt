from django import forms
from django.forms import DateInput
from .models import Booking

class BookingForm (forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'date', 'start_time', 'end_time', 'party_size', 'table', 'notes']
        exclude = ['created_at']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_email': forms.TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'type': 'date'}),
            'start_time': forms.TextInput(attrs={'class': 'form-control'}),
            'end_time': forms.TextInput(attrs={'class': 'form-control'}),
            'party_size': forms.TextInput(attrs={'class': 'form-control'}),
            'table': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }