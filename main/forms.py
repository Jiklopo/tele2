from django.forms import ModelForm
from django.db.models import Q
from main.models import *


class BookableForm(ModelForm):
    class Meta:
        model = Bookable
        fields = ['name', 'rows', 'columns', 'max_filled', 'social_distance']


class BookingForm(ModelForm):
    def clean(self):
        dist = self.cleaned_data['place'].social_distance
        r = self.cleaned_data['row']
        c = self.cleaned_data['column']
        st_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        intersection = ~(Q(start_time__gt=end_time) | Q(end_time__lt=st_time))
        bookings = Booking.objects.filter(intersection, column=c, row=r)
        if bookings:
            raise ValidationError('Это место занято!')

        bookings = Booking.objects.filter(intersection, row__gte=r-dist, row__lte=r-dist, column__gte=c-dist, column__lte=c+dist)
        if bookings:
            raise ValidationError(f'Вы должны соблюдать дистанцию в {dist} мест(а).')

        return self.cleaned_data

    class Meta:
        model = Booking
        fields = ['place', 'row', 'column', 'start_time', 'end_time']
