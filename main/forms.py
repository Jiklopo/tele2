from django.forms import ModelForm
from main.models import *


class BookableForm(ModelForm):
    class Meta:
        model = Bookable
        fields = ['name', 'rows', 'columns', 'max_filled', 'social_distance']


class BookingForm(ModelForm):
    def is_valid(self):
        valid = True


        return valid and super(BookingForm, self).is_valid()

    class Meta:
        model = Booking
        fields = ['place', 'row', 'column', 'start_time', 'end_time']