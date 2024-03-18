from django import forms
from django.forms import DateInput
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking, Table
from datetime import datetime


class BookingForm (forms.ModelForm):
    """
    A Django ModelForm for creating and updating Booking objects.

    Attributes:
        Media: A class containing additional metadata,
        such as JavaScript files.
    """
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
        """
        Initialize the BookingForm instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            request: The request associated with the form.
        """
        self.request = kwargs.pop('request', None)
        super(BookingForm, self).__init__(*args, **kwargs)

    def clean_date(self):
        """
        Clean and validate the 'date' field.

        Returns:
            datetime.date: The cleaned and validated date.

        Raises:
            ValidationError: If the date is not within
            valid restaurant dates or not made in advance.
        """
        date = self.cleaned_data['date']
        current_date = timezone.now().date()
        user = self.request.user

        if not user.is_staff:
            if date <= current_date + timezone.timedelta(days=60):
                raise ValidationError(
                    'Bookings must be made at least 60 days in advance.')

        if date.weekday() not in [1, 2, 3, 4, 5]:
            raise ValidationError(
                'The restaurant is open from Tuesday \
                 to Saturday. Please select a valid date.')

        return date

    def clean(self):
        """
        Clean and validate the entire form.

        Returns:
            dict: The cleaned and validated form data.

        Raises:
            ValidationError: If there are issues with
            date, start_time, or party_size.
        """
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        party_size = cleaned_data.get('party_size')

        if not all ([date, start_time, party_size]):
            raise ValidationError(
                "Please provide date and start time, and party size.")

        current_date = timezone.now().date()
        if date < current_date:
            raise ValidationError(
                "Booking date cannot be in the past. Choose a valid date.")

        tables_with_capacity = Table.objects.filter(
            number_of_seats__gte=party_size
        )

        start_datetime = datetime.combine(date, start_time)

        bookings_on_requested_datetime = Booking.objects.filter(
            date=date,
            start_time__lte=start_datetime,
            start_time__gte=start_datetime - self.get_time_window(date)
        ).exclude(id=self.instance.id)

        booked_tables = [
            booking.table.id for booking in bookings_on_requested_datetime]

        available_tables = tables_with_capacity.exclude(id__in=booked_tables)

        if not available_tables:
            self.add_error(
                'party_size',
                "Sorry! There are no tables \
            available for the selected date and guest number.")
        else:
            chosen_table = available_tables[0]
            self.instance.table = chosen_table

        return cleaned_data

    def get_time_window(self, date):
        """
        Get the time window based on the day of the week.

        Args:
            date (datetime.date): The date
            for which the time window is calculated.

        Returns:
            timezone.timedelta: The calculated time window.
        """

        if date.weekday() == 5:
            return timezone.timedelta(minutes=30)
        elif date.weekday() in [1, 2, 3, 4]:
            return timezone.timedelta(minutes=45)
        else:
            return timezone.timedelta(minutes=60)
