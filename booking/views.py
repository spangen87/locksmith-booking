from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import PlaceBooking, Review, User
from .forms import BookingForm, ReviewForm, EditBooking


# Create your views here.


def get_index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'booking/index.html', context)


def about(request):
    return render(request, 'booking/about.html')


@login_required
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


@login_required
def view_booking(request):
    if request.user.is_staff:
        bookings = PlaceBooking.objects.all()
    else:
        bookings = request.user.bookings.all()
    context = {
        'bookings': bookings,
    }
    return render(request, 'booking/my_account.html', context)


@login_required
def delete_booking(request, booking_id):
    email_to = None
    try:
        booking = get_object_or_404(PlaceBooking, id=booking_id)
        email_to = booking.email
        subject = 'Your booking'
        message = f'Hi {booking.first_name}, your booking has been cancelled.'
        email_from = 'bestlasbooking@gmail.com'
        recipient_list = [email_to, ]
        send_mail(subject, message, email_from, recipient_list)
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
        return redirect('my_account')
    except Http404 as err:
        messages.error(request, 'Oops, booking not found.')
        return redirect('my_account')


@login_required
def edit_booking(request, booking_id):
    email_to = None
    try:
        booking = get_object_or_404(PlaceBooking, id=booking_id)
        if request.method == 'POST':
            form = EditBooking(request.POST, instance=booking)
            if form.is_valid():
                form.save()
                email_to = booking.email
                subject = 'Your booking'
                message = f'Hi {booking.first_name}, your booking has been updated. Log in to see details.'
                email_from = 'bestlasbooking@gmail.com'
                recipient_list = [email_to, ]
                send_mail(subject, message, email_from, recipient_list)
                messages.success(request, 'Updated successfully!')
                return redirect('my_account')
        form = EditBooking(instance=booking)
        context = {
                'form': form
            }
        return render(request, 'booking/edit_booking.html', context)
    except Http404 as err:
        messages.error(request, 'Oops, booking not found.')
        return redirect('my_account')


@login_required
def approve_booking(request, booking_id):
    booking = get_object_or_404(PlaceBooking, id=booking_id)
    booking.approved = not booking.approved
    booking.save()
    email_to = booking.email
    subject = 'Your booking'
    message = f'Hi {booking.first_name}, your booking has been updated. Log in to see details.'
    email_from = 'bestlasbooking@gmail.com'
    recipient_list = [email_to, ]
    send_mail(subject, message, email_from, recipient_list)
    messages.success(request, 'Booking Updated successfully!')
    return redirect('my_account')


@login_required
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


@login_required
def view_review(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'booking/reviews.html', context)


# @login_required
# def delete_review(request, review_id):
#     try:
#         review = get_object_or_404(PlaceBo, id=booking_id)
#         email_to = booking.email
#         subject = 'Your booking'
#         message = f'Hi {booking.first_name}, your booking has been cancelled.'
#         email_from = 'bestlasbooking@gmail.com'
#         recipient_list = [email_to, ]
#         send_mail(subject, message, email_from, recipient_list)
#         booking.delete()
#         messages.success(request, 'Booking deleted successfully.')
#         return redirect('my_account')
#     except Http404 as err:
#         messages.error(request, 'Oops, booking not found.')
#         return redirect('my_account')