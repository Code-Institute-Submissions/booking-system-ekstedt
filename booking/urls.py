from booking import views
from django.urls import path, include

app_name = 'booking'
urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('menu/', views.MenuPage.as_view(), name="menu"),
    path('history/', views.HistoryPage.as_view(), name="history"),
    path('contact/', views.ContactPage.as_view(), name="contact"),
    path('bookings/', views.BookingList.as_view(), name="bookings"),
    path('<int:pk>/', views.BookingDetail.as_view(), name="details"),
    path('create/', views.CreateBooking.as_view(), name="create_booking"),
    path('update/<int:pk>/', views.UpdateBooking.as_view(), name="update"),
    path('delete/<int:pk>/', views.DeleteBooking.as_view(), name="delete_booking"),
    path('profile/', views.Profile.as_view(), name="profile"),
]