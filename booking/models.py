from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Table(models.Model):
    """
    Model representing a dining table in the restaurant.

    Attributes:
    - table_number: The unique identifier for the table.
    - number_of_seats: The number of seats at the table (default is 2).
    """
    table_number = models.IntegerField(unique=True)
    number_of_seats = models.IntegerField(
        validators=[MinValueValidator(2), MaxValueValidator(12)], default=2)

    def __str__(self):
        """
        Returns a string representation of the table.
        """
        return f"Table {self.table_number}"


class Booking(models.Model):
    """
    Model representing a reservation booking for a dining table.

    Attributes:
    - user: The user making the reservation (ForeignKey to Django User model).
    - name: The name associated with the reservation.
    - email: The email address of the user (optional).
    - date: The date of the reservation.
    - start_time: The starting time of the reservation.
    - party_size: The number of people in the reservation (1 to 6).
    - table: The dining table associated
    with the reservation (ForeignKey to Table model).
    - notes: Additional notes or comments for the reservation (optional).
    - created_at: The timestamp when the reservation was created.
    - status: The status of the reservation (Pending, Confirmed, Rejected).
    - confirmation_date: The timestamp when
    the reservation was confirmed (optional).
    - rejection_date: The timestamp when
    the reservation was rejected (optional).
    """
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=150, blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    party_size = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)])
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='Pending')
    confirmation_date = models.DateTimeField(null=True, blank=True)
    rejection_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the reservation.
        """
        return self.name

    def confirm_booking(self):
        """
        Method to confirm the reservation
        and update the status and confirmation date.
        """
        self.status = 'Confirmed'
        self.confirmation_date = timezone.now()
        self.save()

    def reject_booking(self):
        """
        Method to reject the reservation
        and update the status and rejection date.
        """
        self.status = 'Rejected'
        self.rejection_date = timezone.now()
        self.save()

    def update_status(self, status, date):
        """
        Method to update the reservation status and associated date.

        - status (str): The new status for the reservation.
        - date (datetime): The date associated with the new status.
        """
        self.status = status
        setattr(self, f"{status.lower()}_date", date)
        self.save()


class BookingHistory(models.Model):
    """
    Model representing the history of
    actions performed on a reservation booking.

    - ACTION_CHOICES: Choices for the types of actions (confirmed, rejected).
    - booking: The reservation booking associated
    with the history entry (ForeignKey to Booking model.)
    - action: The type of action performed (confirmed, rejected).
    - timestamp: The timestamp when the
    action was recorded (default is the current time).
    - user: The user who performed the
    action (ForeignKey to Django User model, can be null and blank).
    """
    ACTION_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    ]

    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name='history')
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(
            default=timezone.now)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the booking history entry.
        """
        return f"{self.action} on {self.booking} \
        at {self.timestamp} \
        by {self.user}"
