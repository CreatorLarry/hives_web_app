from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'county', 'town', 'place_name', 'event_type', 'specifications',
            'num_people', 'additional_notes', 'contact_number', 'event_date', 'email', 'client_name'
        ]
        widgets = {
            'county': forms.TextInput(attrs={'class': 'form-control border-primary p-2', 'placeholder': 'Enter County'}),
            'town': forms.TextInput(attrs={'class': 'form-control border-primary p-2', 'placeholder': 'Enter Town'}),
            'place_name': forms.TextInput(attrs={'class': 'form-control border-primary p-2', 'placeholder': 'Enter Place Name'}),
            'event_type': forms.Select(attrs={'class': 'form-select border-primary p-2', 'placeholder': 'Select Event Type'}),
            'specifications': forms.TextInput(attrs={'class': 'form-control border-primary p-2', 'placeholder': 'Any Specifications'}),
            'num_people': forms.Select(attrs={'class': 'form-select border-primary p-2', 'placeholder': 'Number of People'}),
            'additional_notes': forms.TextInput(attrs={'class': 'form-control border-primary p-2', 'placeholder': 'Anything Else To Note?'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control border-primary p-2', 'placeholder': 'Your Contact No.'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control border-primary p-2', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border-primary p-2', 'placeholder': 'Enter Your Email'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control border-primary p-2', 'placeholder': 'Enter Your Name'}),
        }
