from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    number_of_seats = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number}"
    
class Booking(models.Model):
    customer_name = models.CharField(max_length = 255)
    contact_number = models.CharField(max_length = 15)
    booking_time = models.DateTimeField()
    party_size = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    image = CloudinaryField('image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.customer_name} by {self.user.username} at {self.booking_time}"