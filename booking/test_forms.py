from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Table, Booking
from .forms import BookingForm
import datetime

class BookingFormTest(TestCase):
    def setUp(self):
        # Creating a user
        self.user = User.objects.create(
            username = 'Testinguser', password='testinguser')

        # Creating some table instances
        self.table1 = Table.objects.create(table_number=5, number_of_seats=2)
        self.table2 = Table.objects.create(table_number=6, number_of_seats=4)
        self.table3 = Table.objects.create(table_number=7, number_of_seats=6)
        self.table4 = Table.objects.create(table_number=8, number_of_seats=2)
        self.table5 = Table.objects.create(table_number=9, number_of_seats=2)

    def create_request(self, user=None):
        # Creating mock request object
        request = RequestFactory().get('/')
        request.user = user
        return request

    def test_valid_data(self):
        # Create a normal booking to see if it is valid
        request = self.create_request(user = self.user)
        form = BookingForm({
            'name': 'Test User',
            'date': datetime.date.today() + datetime.timedelta(days=61),
            'start_time': '12:00', # Using a valid start time
            'party_size': 2,
            'notes': 'This is a test',
        }, request = request)

        print(form.errors)

        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_data(self):
        # Testing with invalid data to check for validation errors
        request = self.create_request(user=self.user)
        form = BookingForm({
            'name': '', # Empty name should trigger a validation error
            'date': datetime.date.today(), # Should trigger a validation error 
            'start_time': '', # Empty start_time should trigger a validation error
            'party_size': 8, # Should trigger a validation error of exceeding the guest number
            'notes': 'This is a test',
        }, request=request)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors) # Checking if 'name' field has a validation error
        self.assertIn('date', form.errors) # Checking if 'date' field has a validation error
        self.assertIn('start_time', form.errors) # Checking if 'start_time' field has a validation error
        self.assertIn('party_size', form.errors) # Checking if 'party_size' field has a validation error