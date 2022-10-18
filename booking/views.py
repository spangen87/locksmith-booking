from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import PlaceBooking, Review
from .forms import BookingForm, ReviewForm

# Create your views here.


def get_index(request):
    return render(request, 'booking/index.html')


def about(request):
    return render(request, 'booking/about.html')


def place_booking(request):
    if request.method == 'POST':
        booking = PlaceBooking(user=request.user)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking placed successfully. Please allow up to 24 hours for callback.')
            return redirect('place_booking')
    else:
        form = BookingForm()
    return render(request, 'booking/place_booking.html', {'form': form})


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
    messages.success(request, 'Booking deleted successfully.')
    # return render(request, 'booking/my_account.html')
    return redirect('my_account')


def edit_booking(request, booking_id):
    booking = get_object_or_404(PlaceBooking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully!')
            return redirect('my_account')
    form = BookingForm(instance=booking)
    context = {
            'form': form
        }
    return render(request, 'booking/edit_booking.html', context)


def approve_booking(request, booking_id):
    booking = get_object_or_404(PlaceBooking, id=booking_id)
    booking.approved = not booking.approved
    booking.save()
    return redirect('my_account')


def place_review(request):
    if request.method == 'POST':
        review = Review(user=request.user)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            # form.instance.name = request.name  ????
            form.save()
            messages.success(request, 'Review posted successfully. Waiting for approval.')
            return redirect('place_review')
    else:
        form = ReviewForm()
        context = {
            'form': form,
            'posted': True
            }
    return render(request, 'booking/place_review.html', context)
