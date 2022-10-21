from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
import datetime


class PlaceBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField()
    email = models.EmailField()
    phone = PhoneNumberField()
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    date_for_visit = models.DateField(null=True)
    time_for_visit = models.TimeField(default=datetime.time(12, 00))

    def save(self, *args, **kwargs):
        if self.date_for_visit < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(PlaceBooking, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.first_name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    name = models.ForeignKey(PlaceBooking, on_delete=models.CASCADE, related_name='reviews')
    approved = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    review = models.TextField()

    class Meta:
        ordering: ['created_on']

    def __str__(self):
        return f"Review {self.review} by {self.name.first_name} {self.name.last_name}"
