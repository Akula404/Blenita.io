import requests
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Contact, TableBooking, Menu, Special, Event, Gallery, Chef, Testimonial
from django.contrib import messages
from django.core.mail import send_mail  # Optional: If you want to send email notifications

# Home Page View
def home(request):
    menus = Menu.objects.all()
    specials = Special.objects.all()
    events = Event.objects.all()
    galleries = Gallery.objects.all()
    chefs = Chef.objects.all()
    testimonials = Testimonial.objects.all()
    
    return render(request, 'index.html', {
        'menus': menus,
        'specials': specials,
        'events': events,
        'galleries': galleries,
        'chefs': chefs,
        'testimonials': testimonials,
    })

# Static Pages Views
def about(request):
    return render(request, 'about.html')

def chef(request):
    return render(request, 'chef.html')

def events(request):
    return render(request, 'events.html')

def gallery(request):
    return render(request, 'gallery.html')

def menu(request):
    return render(request, 'menu.html')

def specials(request):
    return render(request, 'specials.html')

# ---------------------------------
# BOOKING VIEWS (Require Login)
# ---------------------------------

@login_required(login_url='logs_app:login_client')
def book_a_table(request):
    """Handles booking submission"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        people = request.POST.get('people')
        message = request.POST.get('message', '')

        TableBooking.objects.create(
            user=request.user,
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            people=people,
            message=message
        )
        messages.success(request, "Your booking request was sent. Thank you!")
        return redirect('restaurant_app:show_book_a_table')

    return render(request, 'book_a_table.html')

@login_required(login_url='logs_app:login_client')
def show_book_a_table(request):
    """Show only the logged-in user's bookings"""
    bookings = TableBooking.objects.filter(user=request.user).order_by('-id')
    return render(request, 'show_book_a_table.html', {'bookings': bookings})

@login_required(login_url='logs_app:login_client')
def delete_booking(request, booking_id):
    """Allow only the owner to delete a booking"""
    booking = get_object_or_404(TableBooking, id=booking_id, user=request.user)
    booking.delete()
    messages.success(request, "Booking deleted successfully.")
    return redirect('restaurant_app:show_book_a_table')

@login_required(login_url='logs_app:login_client')
def update_booking(request, booking_id):
    """Allow only the owner to update their booking"""
    booking = get_object_or_404(TableBooking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.name = request.POST.get('name', booking.name)
        booking.email = request.POST.get('email', booking.email)
        booking.phone = request.POST.get('phone', booking.phone)
        booking.date = request.POST.get('date', booking.date)
        booking.time = request.POST.get('time', booking.time)
        booking.people = request.POST.get('people', booking.people)
        booking.message = request.POST.get('message', booking.message)
        booking.save()
        messages.success(request, "Booking updated successfully.")
        return redirect('restaurant_app:show_book_a_table')

    return render(request, 'update_booking.html', {'booking': booking})

# ---------------------------------
# CONTACT VIEWS (Require Login)
# ---------------------------------

@login_required(login_url='logs_app:login_client')
def contact(request):
    """Handles contact form submission"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            Contact.objects.create(user=request.user, name=name, email=email, subject=subject, message=message)
            messages.success(request, "Your message has been sent successfully!")
        else:
            messages.error(request, "Please fill in all fields.")

        return redirect('restaurant_app:show_contact')

    return render(request, 'contact.html')

@login_required(login_url='logs_app:login_client')
def show_contact(request):
    """Show only the logged-in user's contact messages"""
    contacts = Contact.objects.filter(user=request.user).order_by('-id')
    return render(request, 'show_contact.html', {'contacts': contacts})

@login_required(login_url='logs_app:login_client')
def contact_detail(request, contact_id):
    """Displays a specific contact message only if it belongs to the logged-in user"""
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)
    return render(request, 'contact_detail.html', {'contact': contact})

@login_required(login_url='logs_app:login_client')
def delete_contact(request, contact_id):
    """Allow only the owner to delete their contact message"""
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)
    contact.delete()
    messages.success(request, "Contact deleted successfully.")
    return redirect('restaurant_app:show_contact')

@login_required(login_url='logs_app:login_client')
def update_contact(request, contact_id):
    """Allow only the owner to update their contact message"""
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)

    if request.method == 'POST':
        contact.name = request.POST.get('name', contact.name)
        contact.email = request.POST.get('email', contact.email)
        contact.subject = request.POST.get('subject', contact.subject)
        contact.message = request.POST.get('message', contact.message)
        contact.save()
        messages.success(request, "Contact updated successfully.")
        return redirect('restaurant_app:show_contact')

    return render(request, 'update_contact.html', {'contact': contact})
