from django.contrib.auth.models import User
from django.db import models


class TableBooking(models.Model):
    # Fields for the table booking form
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link each booking to a user
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField(blank=True)  # Optional message

    def __str__(self):
        return f"Booking for {self.people} people by {self.name} on {self.date} at {self.time}"


class Contact(models.Model):
    # Fields for the contact form
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional user link
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} ({self.email}): {self.subject}"


class Menu(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='photos')
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - Ksh{self.price}"


class Special(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    info = models.CharField(max_length=150)
    img = models.ImageField(upload_to='spices')

    def __str__(self):
        return f"Special: {self.name} ({self.info})"


class Event(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField()
    img = models.ImageField(upload_to='activities')
    offers = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.title} - Ksh{self.price}"


class Gallery(models.Model):
    img = models.ImageField(upload_to='galeria')

    def __str__(self):
        return f"Gallery Image: {self.img.name}"  # Display the file name instead of just the object


class Chef(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='cheftos')

    def __str__(self):
        return f"{self.name}, {self.title}"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return f"Testimonial by {self.name} - {self.title}"
