from .models import PlaceBooking
from django import forms


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
            'date_for_visit': DateInput(),
            'time_for_visit': TimeInput()
        }
