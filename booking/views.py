from django.shortcuts import render, redirect
from .models import PlaceBooking
from .forms import BookingForm

# Create your views here.
def get_index(request):
    return render(request, 'booking/index.html')


def place_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('place_booking')
    form = BookingForm()
    context = {'form': form}
    return render(request, 'booking/place_booking.html', context)       


def view_booking(request):
    bookings = PlaceBooking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/my_account.html', context)
