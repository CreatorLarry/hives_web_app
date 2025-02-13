from django.db import models

# Create your models here.

from django.db import models


class Booking(models.Model):
    county = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    place_name = models.CharField(max_length=200)
    event_type = models.CharField(max_length=50, choices=[
        ('Wedding', 'Wedding'),
        ('Graduation', 'Graduation'),
        ('Private', 'Private '),
        ('Anniversary', 'Anniversary'),
        ('Unspecified', 'Unspecified'),
    ], default='Wedding Event')
    specifications = models.TextField()
    num_people = models.CharField(max_length=50, choices=[
        ('50-100', '50-100'),
        ('100-200', '200-500'),
        ('500-1000', '500-1000'),
        ('1000+', '1000+'),
    ], default="50-100 People")
    additional_notes = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=15)
    event_date = models.DateField()
    email = models.EmailField()
    client_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} event at {self.place_name} - {self.county}, {self.town} booked by {self.client_name}"


class OrderableItem(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='orderable_items/', blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    county = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    place_name = models.CharField(max_length=200)
    items = models.ManyToManyField(OrderableItem, related_name='orders')
    specifications = models.TextField()
    additional_notes = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    client_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.items} ordered by {self.client_name} to be delivered to {self.county}, {self.town} at {self.place_name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
