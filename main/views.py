from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(TemplateView):
    template_name = 'index.html'

class UserLoginView(LoginView):
    pass

class UserRegisterView(CreateView):
    form_class = UserCreationForm

class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass

class UserChangePasswordView(PasswordChangeView):
    pass

class CreateBookableView(CreateView):
    pass

class UpdateBookableView(UpdateView):
    pass

class DeleteBookableView(DeleteView):
    pass

class CreateBookingView(CreateView):
    pass

class UpdateBookingView(UpdateView):
    pass

class DeleteBookingView(DeleteView):
    pass
