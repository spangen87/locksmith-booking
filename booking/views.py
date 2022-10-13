from django.shortcuts import render, redirect, get_object_or_404
from .models import PlaceBooking
from .forms import BookingForm

# Create your views here.
def get_index(request):
    return render(request, 'booking/index.html')


def place_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = PlaceBooking(user=request.user)
            form.save()
            return redirect('place_booking')
    form = BookingForm()
    context = {'form': form}
    return render(request, 'booking/place_booking.html', context)   


def view_booking(request):
    if request.user.is_staff:
        bookings = PlaceBooking.objects.all()
    else:
        bookings = request.user.bookings.all()
    context = {
        'bookings': bookings,
    }
    return render(request, 'booking/my_account.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(PlaceBooking, id=booking_id)
    booking.delete()
    return render(request, 'booking/my_account.html')
