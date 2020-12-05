from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView

from main.models import *
from main.forms import BookableForm, BookingForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['bookables'] = Bookable.objects.all()
        return context


class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')


class UserRegisterView(CreateView):
    template_name = 'auth/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('index')


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('index')


class UserChangePasswordView(PasswordChangeView):
    template_name = 'auth/password.html'
    success_url = reverse_lazy('index')


class CreateBookableView(CreateView):
    template_name = 'bookables/form.html'
    form_class = BookableForm
    success_url = reverse_lazy('index')


class UpdateBookableView(UpdateView):
    template_name = 'bookables/form.html'
    form_class = BookableForm
    queryset = Bookable.objects.all()
    success_url = reverse_lazy('index')


class DeleteBookableView(DeleteView):
    template_name = 'bookables/form.html'
    form_class = BookableForm
    queryset = Bookable.objects.all()
    success_url = reverse_lazy('index')


class CalendarView(DetailView):
    template_name = 'calendar.html'
    queryset = Bookable.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CalendarView, self).get_context_data(**kwargs)
        try:
            context['bookings'] = Booking.objects.get(place=self.object)
        except Booking.DoesNotExist:
            context['bookings'] = []
        return context


class CreateBookingView(CreateView):
    template_name = 'bookings/form.html'
    form_class = BookingForm
    success_url = reverse_lazy('index.html')


class UpdateBookingView(UpdateView):
    template_name = 'bookings/form.html'
    form_class = BookingForm
    queryset = Booking.objects.all()
    success_url = reverse_lazy('index.html')


class DeleteBookingView(DeleteView):
    template_name = 'bookings/form.html'
    form_class = BookingForm
    queryset = Booking.objects.all()
    success_url = reverse_lazy('index.html')
