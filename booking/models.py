from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Table(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    table_number = models.IntegerField(unique=True)
    party_size = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number}"
    
class Booking(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length = 255)
    date = models.DateField()
    start_time= models.TimeField()
    end_time = models.TimeField()
    party_size = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.customer_name} by {self.username.username} at {self.start_time} and {self.end_time}"