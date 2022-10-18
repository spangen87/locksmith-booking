from django.contrib import admin
from .models import PlaceBooking, Review

# Register your models here.
# admin.site.register(PlaceBooking)

@admin.register(PlaceBooking)
class PlaceBookingAdmin(admin.ModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'date_for_visit',
        'time_for_visit',
        'approved'
        )
    list_filter = ('approved', 'date_for_visit', 'created_on')
    search_fields = ('first_name', 'last_name', 'phone', 'email')


@admin.register(Review)
class Review(admin.ModelAdmin):

    list_display = (
        'user',
        'name',
        'approved',
        'created_on',
        'review'
    )
