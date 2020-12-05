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
        intersec = Booking.objects.filter(Q(start_time__gt=end_time) | Q(end_time__lt=st_time))
        bookings = Booking.objects.filter(row=r, column=c).intersection(intersec)
        if bookings:
            raise ValidationError('Это место уже занято в это время!')
        bookings = Booking.objects.filter(row__gt=r-dist, row__lt=r+dist,
                                          column__gt=c-dist, column__lt=c+dist).intersection(intersec)
        if bookings:
            raise ValidationError(f'Необходимо соблюдать дистанцию в {dist} мест(а).')

        return self.cleaned_data

    class Meta:
        model = Booking
        fields = ['place', 'row', 'column', 'start_time', 'end_time']
