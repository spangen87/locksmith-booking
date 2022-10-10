from django.shortcuts import render
from .models import PlaceBooking
from .forms import BookingForm

# Create your views here.
def get_index(request):
    return render(request, 'booking/index.html', {'form': BookingForm()})


def place_booking(request):
    return render(request, 'booking/place_booking.html', {'form': BookingForm()})
    form = BookingForm(data=request.POST)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'booking/place_booking.html')
    