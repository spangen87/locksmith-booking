from .models import PlaceBooking, Review
from django import forms
from phonenumber_field.formfields import PhoneNumberField
import datetime


class DateInput(forms.DateInput):
    """
    Class to make a calender showing when choosing the date.
    Solution found at: https://webpedia.net/how-to-use-datepicker-in-django
     """
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'text'


class BookingForm(forms.ModelForm):
    """
    Presents the booking form to the user.
    Make sure dates to choose from is at
    least two days in future, and a maximum
    of 30 days.
    """
    class Meta:
        model = PlaceBooking
        fields = ('first_name',
                  'last_name',
                  'address',
                  'email',
                  'phone',
                  'description',
                  'date_for_visit',
                  'time_for_visit',)
        widgets = {
            'date_for_visit': DateInput(attrs={
                'min': datetime.date.today()+datetime.timedelta(days=2),
                'max': datetime.date.today()+datetime.timedelta(days=30)}),
            'time_for_visit': TimeInput(attrs={
                'class': 'timepicker'}),
        }


class EditBooking(forms.ModelForm):
    """
    The same as place booking form above.
    But without the restrictions of at least
    two days in the future. That because a
    staff member should be able to update
    the booking after that if needed.
    """
    class Meta:
        model = PlaceBooking
        fields = ('first_name',
                  'last_name',
                  'address',
                  'email',
                  'phone',
                  'description',
                  'date_for_visit',
                  'time_for_visit',)
        widgets = {
            'date_for_visit': DateInput(attrs={
                'min': datetime.date.today(),
                'max': datetime.date.today()+datetime.timedelta(days=30)}),
            'time_for_visit': TimeInput()
        }


class ReviewForm(forms.ModelForm):
    """
    Presents the form for placing a review
    to the user.
    """
    class Meta:
        model = Review
        fields = ('review',)
