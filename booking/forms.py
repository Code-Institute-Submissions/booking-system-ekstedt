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

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(BookingForm, self).__init__(*args, **kwargs)

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

        # Checks if date and start_time are not none
        if date is None or start_time is None or party_size is None:
            raise ValidationError("Please provide both date and start time, and party size.")

        # Ensures the selected date is not in the past
        current_date = timezone.now().date()
        if date < current_date:
            raise ValidationError("Booking date cannot be in the past. Choose a valid date.")

        # Filters tables with capacity greater or equal to the party size
        tables_with_capacity = Table.objects.filter(
            number_of_seats__gte=party_size
        )

        # Converts start_time to datetime object for comparison
        start_datetime = datetime.combine(date, start_time)

        # Gets bookings on the specified date excluding the current booking that is being updated
        bookings_on_requested_datetime = Booking.objects.filter(
            date=date,
            start_time__lte=start_datetime,
            start_time__gte=start_datetime - self.get_time_window(date)
        ).exclude(id=self.instance.id)

        # Gets booked tables for the specified datetime
        booked_tables = [booking.table.id for booking in bookings_on_requested_datetime]

        # Filters available tables by excluding booked tables
        available_tables = tables_with_capacity.exclude(id__in=booked_tables)

        # Throws validation error if no tables are available
        if not available_tables:
            raise ValidationError("Sorry! There are no tables available for the selected date and guest number.")  

        chosen_table = available_tables[0]

        self.instance.table = chosen_table

        return cleaned_data

    def get_time_window(self, date):
        # Adjusts the time window based on the day of the week
        if date.weekday() == 5: # Saturday
            return timezone.timedelta(minutes=30)
        elif date.weekday() in [1, 2, 3, 4]:
            return timezone.timedelta(minutes=45)
        else:
            return timezone.timedelta(minutes=60)