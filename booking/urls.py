from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookingIndex.as_view(), name="booking index"),
]