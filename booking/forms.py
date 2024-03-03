from django import forms
from django.forms import DateInput
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking, Table
from datetime import datetime

class BookingForm (forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'start_time', 'party_size', 'notes']
        exclude = ['created_at']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'type': 'date'}),
            'start_time': forms.Select(attrs={'class': 'form-control'}),
            'party_size': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }

    class Media:
        js = ('static/js/booking_form.js')

    def clean_date(self):
        date = self.cleaned_data['date']
        current_date = timezone.now().date()
        user = self.request.user

        if not user.is_staff:
            if date <= current_date + timezone.timedelta(days=60):
                raise ValidationError('Bookings must be made at least 60 days in advance.')

        # Check if the selected date is within valid restaurant dates (Tuesday to Saturday).
        if date.weekday() not in [1, 2, 3, 4, 5]:
            raise ValidationError('The restaurant is open from Tuesday to Saturday. Please select a valid date.')

        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        party_size = cleaned_data.get('party_size')

        # Filter tables with capacity greater or equal to the party size
        tables_with_capacity = Table.objects.filter(
            number_of_seats__gte=party_size
        )

        # Check if date and start_time are not none
        if date is None or start_time is None:
            
            raise ValidationError("Please provide both date and start time.")

        # Converting start_time to datetime object for comparison
        start_datetime = datetime.combine(date, start_time)

        # Get bookings on the specified date excluding the current booking that is being updated
        bookings_on_requested_datetime = Booking.objects.filter(
            date=date,
            start_time__lte=start_datetime,
            start_time__gte=start_datetime - self.get_time_window(date)
        ).exclude(id=self.instance.id)

        # Iterate over bookings to get tables not booked
        available_tables = []
        for table in tables_with_capacity:
            is_table_booked = any(
                table.id == booking.table.id
                for booking in bookings_on_requested_datetime
            )
            if not is_table_booked:
                available_tables.append(table)

        # Throw validation error if no tables are available
        if not available_tables:
            raise ValidationError("Sorry! There are no tables available for the selected date and guest number.")  

        chosen_table = available_tables[0]

        self.instance.table = chosen_table

        return cleaned_data

    def get_time_window(self, date):
        # Adjust the time window based on the day of the week
        if date.weekday() == 5: # Saturday
            return timezone.timedelta(minutes=30)
        elif date.weekday() in [1, 2, 3, 4]:
            return timezone.timedelta(minutes=45)
        else:
            return timezone.timedelta(minutes=60)