from django import forms
from django.forms import DateInput
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking, Table

class BookingForm (forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'start_time', 'party_size', 'notes']
        exclude = ['created_at']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'type': 'date'}),
            'start_time': forms.TextInput(attrs={'class': 'form-control'}),
            'party_size': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        current_date = timezone.now().date()
        user = self.request.user

        if not user.is_staff:
            if date <= current_date + timezone.timedelta(days=60):
                raise ValidationError('Bookings must be made at least 60 days in advance.')

        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        party_size = cleaned_data.get('party_size')

        # Filter tables with capacity greater or equal to the party size
        tables_with_capacity = Table.objects.filter(
            number_of_seats__gte=party_size
        )

        # Get bookings on the specified date
        bookings_on_requested_date = Booking.objects.filter(
            date=date
        )

        # Iterate over bookings to get tables not booked
        available_tables = []
        for table in tables_with_capacity:
            is_table_booked = any(
                table.id == booking.table.id
                for booking in bookings_on_requested_date
            )
            if not is_table_booked:
                available_tables.append(table)

        # Throw validation error if no tables are available
        if not available_tables:
            raise ValidationError("Sorry! There are no tables available for the selected date and guest number.")  

        chosen_table = available_tables[0]

        self.instance.table = chosen_table

        return cleaned_data