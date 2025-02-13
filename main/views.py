from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from main.forms import BookingForm, OrderForm
from main.models import Booking, Order, ContactMessage


# Landing Page
def landing_page(request):
    return render(request, 'landing_page.html')


# Booking Views
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
        return render(request, 'booking.html', {'form': form})
    else:
        form = BookingForm()
        return render(request, 'booking.html', {'form': form})


def thank_you(request):
    return render(request, 'thank_you.html', {'message': 'Thank you for your booking!'})


# Static Pages
def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def events(request):
    return render(request, 'events.html')


def menu(request):
    return render(request, 'menu.html')


# Order Views
def order_form(request):
    """Display the empty order form."""
    form = OrderForm()
    return render(request, 'order_detail.html', {'form': form})


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_detail_view')
        return render(request, 'order.html', {'form': form})
    else:
        form = OrderForm()
        return render(request, 'order.html', {'form': form})


def order_detail_view(request):
    """Display order details from session."""
    order_data = request.session.get('order_data')
    if not order_data:
        return redirect('thank_you_order')
    return render(request, 'order_detail.html', {'order_data': order_data})


def order_confirm_view(request):
    """Confirm and save the order."""
    if request.method == 'POST':
        order_data = request.session.get('order_data')
        if order_data:
            items = order_data.pop('items', None)
            order = Order.objects.create(**order_data)
            if items:
                order.items.set(items)
            order.save()
            del request.session['order_data']
            return redirect('thank_you_order')
    return redirect('order_form')


def order_list(request):
    """List previous orders."""
    email = request.GET.get('email')
    orders = Order.objects.filter(email=email) if email else Order.objects.all()
    return render(request, 'previous_order_list.html', {'orders': orders})


def thank_you_order(request):
    """Display thank-you page for orders."""
    return render(request, 'thank_you_order.html')


def contact_view(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print(f"Received Data - Name: {name}, Email: {email}, Message: {message}")

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent. Thank you!")
            return redirect("contact")  # Prevents duplicate submissions on refresh
        else:
            messages.error(request, "All fields are required.")

    return render(request, "contact.html")
