from . import views
from django.urls import path, include

app_name = 'booking'
urlpatterns = [
    path('', views.BookingList.as_view(), name="home"),
    path('<int:pk>/', views.BookingDetail.as_view(), name="details"),
    path('create/', views.CreateBooking.as_view(), name="create_booking")    
]