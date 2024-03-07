from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
from django.apps import apps
from .models import Booking

@receiver(post_save, sender='booking.Booking')
def send_notification_on_confirmation(sender, instance, **kwargs):
    if instance.status == 'Confirmed' and instance.username:
        message = f"Your booking for {instance.date} at {instance.start_time} has been confirmed!"
        apps.get_app_config('booking').messages.success(instance.username, message)

