from django.forms import ModelForm
from main.models import *


class BookableForm(ModelForm):
    class Meta:
        model = Bookable
        fields = ['name', 'rows', 'columns', 'max_filled', 'social_distance']


class BookingForm(ModelForm):
    def is_valid(self):
        valid = super(BookingForm, self).is_valid()
        return valid

    class Meta:
        model = Booking
        fields = ['start_time', 'end_time']