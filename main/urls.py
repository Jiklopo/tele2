from main.views import *
from django.urls import path
urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('register', UserRegisterView.as_view(), name='register'),
    path('change_password', UserChangePasswordView.as_view(), name='change_password'),

    path('bookables/create', CreateBookableView.as_view(), name='bookable-create'),
    path('bookables/<int:pk>/update', UpdateBookableView.as_view(), name='bookable-update'),
    path('bookables/<int:pk>/delete', DeleteBookableView.as_view(), name='bookable-delete'),

    path('bookings/create', CreateBookingView.as_view(), name='booking-create'),
    path('bookings/<int:pk>/update', UpdateBookingView.as_view(), name='booking-update'),
    path('bookings/<int:pk>/delete', DeleteBookingView.as_view(), name='booking-delete'),
]