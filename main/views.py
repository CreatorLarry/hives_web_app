from django.contrib import messages
from django.shortcuts import render, redirect

from main.forms import BookingForm
from main.models import Booking


# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('thank_you')  # Redirect to the thank you page
        else:
            # If the form is invalid, render the form with errors
            return render(request, 'booking.html', {'form': form})
    else:
        # For GET requests, render the empty form
        form = BookingForm()
        return render(request, 'booking.html', {'form': form})


def thank_you(request):
    return render(request, 'thank_you.html', {'message': 'Thank you for your booking!'})


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def events(request):
    return render(request, 'events.html')


def menu(request):
    return render(request, 'menu.html')


def contact(request):
    return render(request, 'contact.html')