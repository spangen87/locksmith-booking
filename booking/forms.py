from .models import PlaceBooking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingForm
        fields = ('first_name', 'last_name', 'address', 'email', 'phone', 'description', 'date_for_visit', 'time_for_visit',)
        