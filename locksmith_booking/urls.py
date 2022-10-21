"""locksmith_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_index, name='home'),
    path('place_booking', views.place_booking, name='place_booking'),
    path('accounts/', include('allauth.urls')),
    path('my_account', views.view_booking, name='my_account'),
    path('delete/<booking_id>', views.delete_booking, name='delete'),
    path('edit_booking/<booking_id>', views.edit_booking, name='edit'),
    path('approve/<booking_id>', views.approve_booking, name='approve'),
    path('place_review', views.place_review, name='place_review'),
    path('about', views.about, name='about'),
    path('reviews', views.view_review, name='reviews'),
    path('delete_review/<review_id>', views.delete_review, name='delete_review'),
    path('users', views.view_users, name='users'),
    path('delete_user/<user_id>', views.delete_user, name='delete_user'),
    path('staff_status/<user_id>', views.toggle_staff, name='staff_status'),
]

handler404 = 'booking.views.error_404'
