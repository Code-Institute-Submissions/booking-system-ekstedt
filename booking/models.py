from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    number_of_seats = models.IntegerField(validators=[MinValueValidator (2), MaxValueValidator(12)], default=2)

    def __str__(self):
        return f"Table {self.table_number}"
    
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length= 150, blank=True, null= True)
    date = models.DateField()
    start_time= models.TimeField()
    party_size = models.IntegerField(validators=[MinValueValidator (1), MaxValueValidator(6)])
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    confirmation_date = models.DateTimeField(null=True, blank=True)
    rejection_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def confirm_booking(self):
        self.status = 'Confirmed'
        self.confirmation_date = timezone.now()
        self.save()

    def reject_booking(self):
        self.status = 'Rejected'
        self.rejection_date = timezone.now()
        self.save()