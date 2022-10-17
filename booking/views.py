from django.shortcuts import render, redirect, get_object_or_404
from .models import PlaceBooking, Review
from .forms import BookingForm, ReviewForm

# Create your views here.
def get_index(request):
    return render(request, 'booking/index.html')


def place_booking(request):
    if request.method == 'POST':
        booking = PlaceBooking(user=request.user)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
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


def edit_booking(request, booking_id):
    booking = get_object_or_404(PlaceBooking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return render(request, 'booking/my_account.html')
    form = BookingForm(instance=booking)
    context = {
            'form': form
        }
    return render(request, 'booking/edit_booking.html', context)


def approve_booking(request, booking_id):
    booking = get_object_or_404(PlaceBooking, id=booking_id)
    booking.approved = not booking.approved
    booking.save()
    return render(request, 'booking/my_account.html')


def place_review(request):
    if request.method == 'POST':
        review = Review(user=request.user)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            # form.instance.name = request.name.first_name  Denna måste lösas!!
            form.save()
            return redirect('place_booking')
    form = ReviewForm()
    context = {'form': form}
    return render(request, 'booking/place_review.html', context)
