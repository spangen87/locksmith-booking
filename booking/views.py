from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import PlaceBooking, Review
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


def error_404(request, exception):
    return render(request, 'booking/404.html')


@login_required
def place_booking(request):
    """
    Views the booking form and checks that the
    input is valid before submitting. If it is
    not, a message will show and redirect back
    to the form.
    """
    if request.method == 'POST':
        booking = PlaceBooking(user=request.user)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking placed successfully.\
                 Please allow up to 24 hours for callback.')
            return redirect('place_booking')
    else:
        form = BookingForm()
    return render(request, 'booking/place_booking.html', {'form': form})


@login_required
def view_booking(request):
    """
    Lets staff member view all bookings, and
    regular user only his own bookings.
    """
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
    """
    Deletes booking and sends an email to the user who placed it.
    John at tutor support helped med figure out this one.
    """
    email_to = None
    if request.user.is_staff:
        try:
            booking = get_object_or_404(PlaceBooking, id=booking_id)
            email_to = booking.email
            subject = 'Your booking'
            message = f'Hi {booking.first_name}, your booking on\
                {booking.date_for_visit} has been cancelled.'
            email_from = 'bestlasbooking@gmail.com'
            recipient_list = [email_to, ]
            send_mail(subject, message, email_from, recipient_list)
            booking.delete()
            messages.success(request, 'Booking deleted successfully.')
            return redirect('my_account')
        except Http404 as err:
            messages.error(request, 'Oops, booking not found.')
            return redirect('my_account')
    else:
        return redirect('home')


@login_required
def edit_booking(request, booking_id):
    """
    Presents the booking form with the recent informtion added.
    When update is done the user gets an email that an update
    has been made.
    """
    email_to = None
    try:
        booking = get_object_or_404(PlaceBooking, id=booking_id)
        if request.method == 'POST':
            form = EditBooking(request.POST, instance=booking)
            if form.is_valid():
                form.save()
                email_to = booking.email
                subject = 'Your booking'
                message = f'Hi {booking.first_name}, your booking on\
                        {booking.date_for_visit} has been updated.\
                        Log in to see details.\
                        Log in: https://locksmith-booking.herokuapp.com/'
                email_from = 'bestlasbooking@gmail.com'
                recipient_list = [email_to, ]
                send_mail(subject, message, email_from, recipient_list)
                messages.success(request, 'Updated successfully!')
                return redirect('my_account')
        else:
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
    """
    Let staff members approve a booking
    or withdraw an approved booking.
    User gets an email that a update has been made.
    """
    if request.user.is_staff:
        booking = get_object_or_404(PlaceBooking, id=booking_id)
        booking.approved = not booking.approved
        booking.save()
        email_to = booking.email
        subject = 'Your booking'
        message = f'Hi {booking.first_name}, your booking on\
            {booking.date_for_visit} has been updated.\
            Log in to see details.\
            Log in: https://locksmith-booking.herokuapp.com/'
        email_from = 'bestlasbooking@gmail.com'
        recipient_list = [email_to, ]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Booking Updated successfully!')
        return redirect('my_account')
    else:
        return redirect('home')


@login_required
def place_review(request):
    """
    Presents the review form if user is logged in.
    Checks that it is valid and throws a message
    if it is not.
    """
    if request.method == 'POST':
        review = Review(user=request.user)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Review posted successfully. Waiting for approval.'
                )
            return redirect('place_review')
        else:
            messages.error(
                request, 'Review must contain valid text. Try again.'
                )
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
    """
    Let staff members view all reviews.
    """
    if request.user.is_staff:
        reviews = Review.objects.all()
        context = {
            'reviews': reviews,
        }
        return render(request, 'booking/reviews.html', context)
    else:
        return redirect('home')


@login_required
def delete_review(request, review_id):
    """
    Let staff members delete a review.
    If it does not exist, a message is shown.
    """
    if request.user.is_staff:
        try:
            review = get_object_or_404(Review, id=review_id)
            review.delete()
            messages.success(request, 'Review deleted successfully.')
            return redirect('reviews')
        except Http404 as err:
            messages.error(request, 'Oops, review not found.')
            return redirect('reviews')
    else:
        return redirect('home')


@login_required
def view_users(request):
    """
    Let staff memebers view all the users.
    """
    if request.user.is_staff:
        users = User.objects.all()
        context = {
            'users': users,
        }
        return render(request, 'booking/users.html', context)
    else:
        return redirect('home')


@login_required
def delete_user(request, user_id):
    """
    Let staff member delete a user.
    If the user does not exist, a message
    will show.
    """
    if request.user.is_staff:
        try:
            user = get_object_or_404(User, id=user_id)
            user.delete()
            messages.success(request, 'User deleted successfully.')
            return redirect('users')
        except Http404 as err:
            messages.error(request, 'Oops, user not found.')
            return redirect('users')
    else:
        messages.error(request, 'You do not have permission to do this.')
        return redirect('home')


@login_required
def toggle_staff(request, user_id):
    """
    Make it possible to give user staff status,
    or remove it. User gets an email that a
    change has been made.
    """
    if request.user.is_staff:
        user = get_object_or_404(User, id=user_id)
        user.is_staff = not user.is_staff
        user.save()
        email_to = user.email
        subject = 'Your status has changed'
        message = f'Hi {user.username}, your authorization has changed.\
            Log in: https://locksmith-booking.herokuapp.com/'
        email_from = 'bestlasbooking@gmail.com'
        recipient_list = [email_to, ]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'User Updated successfully!')
        return redirect('users')
    else:
        messages.error(request, 'You do not have permission for this.')
        return redirect('home')


@login_required
def approve_review(request, review_id):
    """
    Make it possible to approve a review so it will
    show on the home page. Or remove a review from
    the home page.
    """
    review = get_object_or_404(Review, id=review_id)
    review.approved = not review.approved
    review.save()
    messages.success(request, 'Review status updated successfully!')
    return redirect('reviews')
