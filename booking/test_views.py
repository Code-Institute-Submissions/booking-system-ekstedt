from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Booking, Table
from datetime import date
from .messages import BOOKING_SUCCESSFUL_CREATE, BOOKING_SUCCESSFUL_UPDATE, BOOKING_SUCCESSFUL_DELETE
from django.contrib import messages
from django.contrib.messages import get_messages
from django.utils import timezone

class BaseTest(TestCase):
    """
    Base test class for common setup.
    """
    def setUp(self):
        """
        Set up common objects for testing.
        """
        self.user = User.objects.create_user(
            username = 'test_user',
            password = 'test_password'
        )

        self.staff_user = User.objects.create_user(
            username = 'staff_user',
            password = 'staff_password',
            is_staff = True
        )

        self.table = Table.objects.create(table_number=1, number_of_seats=4)

        Booking.objects.create(
            user = self.user,
            table = self.table,
            name = 'Test Guest',
            date = date.today() + timezone.timedelta(days=1),
            start_time = '12:00',
            party_size = 2,
            email = 'test@example.com'
        )

class TestBookingList(BaseTest):
    """
    Test cases for the BookingList view.
    """
    def test_booking_list_view_authenticated_user(self):
        """
        Test if the booking list view is accessible for authenticated users.
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('booking:bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html')

    def test_booking_list_view_staff_user(self):
        """
        Test if the booking list view is accessible for staff users.
        """
        self.client.login(username='staff_user', password='staff_password')
        response = self.client.get(reverse('booking:bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html')

class TestCreateBooking(BaseTest):
    """
    Test cases for the CreateBooking view.
    """
    def test_create_booking_view_authenticated_user(self):
        """
        Test if the create booking view is
        accessible for authenticated users.
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('booking:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')

    def test_create_booking_success(self):
        """
        Test if a new booking is created successfully.
        """
        self.client.login(username = 'test_user', password='test_password')
        response = self.client.post(reverse('booking:create'), {
            'table': self.table.id,
            'name': 'New Guest',
            'date': date.today() + timezone.timedelta(days=61),
            'start_time': '12:00',
            'party_size': 3,
            'email': 'new_guest@example.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 2)
        self.assertEqual(list(messages.get_messages(response.wsgi_request))[0].message, BOOKING_SUCCESSFUL_CREATE)

class TestUpdateBooking (BaseTest):
    """
    Test cases for the UpdateBooking view.
    """
    def test_update_booking_view_authenticated_user(self):
        """
        Test if the update booking view is accessible for authenticated users.
        """
        booking = Booking.objects.get(id=1)
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('booking:update', args=[booking.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update.html')

    def test_update_booking_success(self):
        """
        Test if an existing booking is updated successfully.
        """
        booking = Booking.objects.get(id=1)
        self.client.login(username='test_user', password='test_password')
        response = self.client.post(reverse('booking:update', args=[booking.id]), {
            'table': self.table.id,
            'name': 'Updated Guest',
            'date': date.today() + timezone.timedelta(days=61),
            'start_time': '12:00',
            'party_size': '4',
            'email': 'updated_guest@example.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.get(id=1).name, 'Updated Guest')
        self.assertEqual(list(messages.get_messages(response.wsgi_request))[0].message, BOOKING_SUCCESSFUL_UPDATE)

class TestDeleteBooking(BaseTest):
    """
    Test cases for the DeleteBooking view.
    """
    def test_delete_booking_view_authenticated_user(self):
        """
        Test if the delete booking view is accessible for authenticated users.
        """
        booking = Booking.objects.get(id=1)
        self.client.login(username = 'test_user', password = 'test_password')
        response = self.client.get(reverse('booking:delete', args = [booking.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')

    def test_delete_booking_success(self):
        """
        Test if an existing booking is deleted successfully.
        """
        booking = Booking.objects.get(id=1)
        self.client.login(username = 'test_user', password = 'test_password')
        response = self.client.post(reverse('booking:delete', args = [booking.id]))
        self.assertEqual(response.status_code, 302)
        redirected_response = self.client.get(response.url)
        self.assertEqual(redirected_response.status_code, 200)
        self.assertEqual(Booking.objects.count(), 0)
        storage = get_messages(redirected_response.wsgi_request)
        self.assertEqual(list(storage)[0].message, BOOKING_SUCCESSFUL_DELETE)