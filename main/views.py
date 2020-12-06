from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
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


class UserChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'auth/password.html'
    success_url = reverse_lazy('index')


class CreateBookableView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'bookables/form.html'
    permission_required = 'main.add_bookable'
    form_class = BookableForm
    success_url = reverse_lazy('index')


class UpdateBookableView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'bookables/form.html'
    permission_required = 'main.change_bookable'
    form_class = BookableForm
    queryset = Bookable.objects.all()
    success_url = reverse_lazy('index')


class DeleteBookableView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'bookables/form.html'
    permission_required = 'main.delete_bookable'
    form_class = BookableForm
    queryset = Bookable.objects.all()
    success_url = reverse_lazy('index')


class CalendarView(LoginRequiredMixin, DetailView):
    template_name = 'calendar.html'
    queryset = Bookable.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CalendarView, self).get_context_data(**kwargs)
        try:
            context['bookings'] = Booking.objects.filter(place=self.object)
        except Booking.DoesNotExist:
            context['bookings'] = []
        return context


class CreateBookingView(LoginRequiredMixin, CreateView):
    template_name = 'bookings/form.html'
    form_class = BookingForm
    success_url = reverse_lazy('index.html')

    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = self.request.user
        #booking.place = get_object_or_404(Bookable, id=self.kwargs['pk'])
        booking.save()
        return HttpResponseRedirect(reverse('calendar', args=[booking.place_id]))


class UpdateBookingView(LoginRequiredMixin, UpdateView):
    template_name = 'bookings/form.html'
    form_class = BookingForm
    success_url = reverse_lazy('index.html')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class DeleteBookingView(LoginRequiredMixin, DeleteView):
    template_name = 'bookings/form.html'
    form_class = BookingForm
    success_url = reverse_lazy('index.html')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
