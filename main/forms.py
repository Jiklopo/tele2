from django.forms import ModelForm
from main.models import *


class BookableForm(ModelForm):
    class Meta:
        model = Bookable
        fields = ['name', 'rows', 'columns', 'max_filled', 'social_distance']


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['place', 'start_time', 'end_time']