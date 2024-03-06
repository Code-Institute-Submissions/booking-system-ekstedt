from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking
from django.contrib import messages

def send_notification_on_confirmation(sender, instance, **kwargs):
    if instance.status == 'Confirmed' and instance.username:
        message = f"Your booking for {instance.date} at {instance.start_time} has been confirmed!"
        messages.success(instance.username, message)

