from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Table, Booking
from .forms import BookingForm
import datetime


class BookingFormTest(TestCase):
    def setUp(self):
        """
        Set up initial data for the tests.
        """
        self.user, created = User.objects.get_or_create(
            username='Testinguser', defaults={'password': 'testinguser'}
        )

        # Creating some table instances
        self.table1 = Table.objects.create(table_number=1, number_of_seats=2)
        self.table2 = Table.objects.create(table_number=2, number_of_seats=4)
        self.table3 = Table.objects.create(table_number=3, number_of_seats=6)
        self.table4 = Table.objects.create(table_number=4, number_of_seats=2)
        self.table5 = Table.objects.create(table_number=5, number_of_seats=2)

    def create_request(self, user=None):
        """
        Create a mock request object for testing.

        Parameters:
        - user: User object (default is None)
        """
        request = RequestFactory().get('/')
        request.user = user
        return request

    def test_valid_data(self):
        """
        Test the form with valid data.
        """
        request = self.create_request(user=self.user)
        form = BookingForm({
            'name': 'Test User',
            'date': datetime.date.today() + datetime.timedelta(days=61),
            'start_time': '12:00',
            'party_size': 2,
            'notes': 'This is a test',
        }, request=request)

        print(form.errors)

        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_data(self):
        """
        Test the form with invalid data to check for validation errors.
        """
        request = self.create_request(user=self.user)
        form = BookingForm({
            'name': '',
            'date': datetime.date.today(),
            'start_time': '',
            'party_size': 8,
            'notes': 'This is a test',
        }, request=request)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('date', form.errors)
        self.assertIn('start_time', form.errors)
        self.assertIn('party_size', form.errors)

    def test_past_date(self):
        """
        Test the form with a past date, expecting a validation error.
        """
        request = self.create_request(user=self.user)
        form = BookingForm({
            'name': 'Testing User',
            'date': datetime.date.today() - datetime.timedelta(days=1),
            'start_time': '12:00',
            'party_size': 2,
            'notes': 'This is a test',
        }, request=request)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "Please provide date and start time, and party size.",
            form.errors['__all__'])

    def test_invalid_number_of_guests(self):
        """
        Test the form with an invalid
        number of guests, expecting a validation error.
        """
        request = self.create_request(user=self.user)
        form = BookingForm({
            'name': 'Test User',
            'date': datetime.date.today() + datetime.timedelta(days=61),
            'start_time': '12:00',
            'party_size': 20,
            'notes': 'This is a test',
        }, request=request)

        self.assertFalse(form.is_valid())

        if 'party_size' in form.errors:
            expected_error = 'Sorry! There are no tables \
            available for the selected date and guest number.'
            actual_error = str(form.errors['party_size'][0])
            self.assertEqual(expected_error, actual_error)
        elif 'non_field_errors' in form.errors:
            self.assertIn('Sorry! There are no tables \
            available for the selected date and guest \
            number.', form.errors['non_field_errors'][0])
        else:
            self.fail("Expected error not found in form.errors.")

    def test_all_tables_reserved(self):
        """
        Test when all tables are reserved, expecting a validation error.
        """
        user = self.user

        Booking.objects.create(
            user=user,
            table=self.table1,
            name='Test User',
            date=datetime.date.today() + datetime.timedelta(days=61),
            start_time='12:00',
            notes='Test Reservation',
            party_size=2,
        )

        Booking.objects.create(
            user=user,
            table=self.table2,
            name='Test User2',
            date=datetime.date.today() + datetime.timedelta(days=61),
            start_time='12:00',
            notes='Test Reservation',
            party_size=2,
        )

        Booking.objects.create(
            user=user,
            table=self.table3,
            name='Test User3',
            date=datetime.date.today() + datetime.timedelta(days=61),
            start_time='12:00',
            notes='Test Reservation',
            party_size=2,
        )

        Booking.objects.create(
            user=user,
            table=self.table4,
            name='Test User4',
            date=datetime.date.today() + datetime.timedelta(days=61),
            start_time='12:00',
            notes='Test Reservation',
            party_size=2,
        )

        Booking.objects.create(
            user=user,
            table=self.table5,
            name='Test User5',
            date=datetime.date.today() + datetime.timedelta(days=61),
            start_time='12:00',
            notes='Test Reservation',
            party_size=2,
        )

        # Trying to create a new booking
        form = BookingForm({
            'name': 'Test User',
            'date': datetime.date.today() + datetime.timedelta(days=61),
            'start_time': '12:00',
            'party_size': 2,
            'notes': 'This is a test',
        }, request=self.create_request(user=user))

        self.assertFalse(form.is_valid())

        if 'party_size' in form.errors:
            expected_error = 'Sorry! There are no tables \
            available for the selected date and guest number.'
            actual_error = str(form.errors['party_size'][0])
            self.assertEqual(expected_error, actual_error)
        elif 'non_field_errors' in form.errors:
            self.assertIn('Sorry! There are no tables \
            available for the selected date and guest \
            number.', form.errors['non_field_errors'][0])
        else:
            self.fail("Expected error not found in form.errors.")

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that the fields in the form are explicitly
        defined in the form's Meta class.
        """
        form = BookingForm()
        self.assertEqual(
            form.Meta.fields,
            ['name', 'email', 'date', 'start_time', 'party_size', 'notes']
        )
