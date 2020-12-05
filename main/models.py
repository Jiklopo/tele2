from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

def percentage_validation(value):
    if not 0 <= value <= 100:
        raise ValidationError(f'Value must be in range 0-100. Got {value}')


def positive_integer(value):
    if value <= 1:
        raise ValidationError(f'Value must more than 0.')


def non_negative_integer(value):
    if value <= 0:
        raise ValidationError(f'Value must equal to or more than 0.')


class Bookable (models.Model):
    name = models.CharField(max_length=64)
    rows = models.IntegerField(validators=[positive_integer])
    columns = models.IntegerField(validators=[positive_integer])
    max_filled = models.IntegerField(validators=[percentage_validation])
    social_distance = models.IntegerField(validators=[non_negative_integer])


class Booking(models.Model):
    place = models.ForeignKey(to=Bookable, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()