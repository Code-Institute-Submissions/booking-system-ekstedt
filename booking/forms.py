from django import forms
from django.forms import DateInput
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking

class BookingForm (forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'start_time', 'party_size', 'table', 'notes']
        exclude = ['created_at']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'type': 'date'}),
            'start_time': forms.TextInput(attrs={'class': 'form-control'}),
            'party_size': forms.TextInput(attrs={'class': 'form-control'}),
            'table': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        current_date = timezone.now().date()

        if date <= current_date + timezone.timedelta(days=60):
            raise ValidationError('Bookings must be made at least 60 days in advance.')

        return date