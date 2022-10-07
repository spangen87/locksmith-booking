from django.db import models
from django.contrib.auth.models import User


class PlaceBooking(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    date_for_visit = models.DateField()
    time_for_visit = models.TimeField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.first_name
    
