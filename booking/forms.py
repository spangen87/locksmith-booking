from .models import PlaceBooking, Review
from django import forms
import datetime


class DateInput(forms.DateInput):
    """
    Class to make a calender showing when choosing the date.
    Solution found at: https://webpedia.net/how-to-use-datepicker-in-django
     """
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookingForm(forms.ModelForm):
    class Meta:
        model = PlaceBooking
        fields = ('first_name', 'last_name', 'address', 'email', 'phone', 'description', 'date_for_visit', 'time_for_visit',)
        widgets = {
            'date_for_visit': DateInput(attrs={'min': datetime.date.today()+datetime.timedelta(days=2), 'max': ''}),
            'time_for_visit': TimeInput()
        }


class EditBooking(forms.ModelForm):
    class Meta:
        model = PlaceBooking
        fields = ('first_name', 'last_name', 'address', 'email', 'phone', 'description', 'date_for_visit', 'time_for_visit',)
        widgets = {
            'date_for_visit': DateInput(attrs={'min': datetime.date.today()}),
            'time_for_visit': TimeInput()
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review', 'name')
