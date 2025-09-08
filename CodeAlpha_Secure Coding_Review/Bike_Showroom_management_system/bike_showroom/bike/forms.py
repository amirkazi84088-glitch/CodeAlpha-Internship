# bike/forms.py
from django import forms
from .models import Booking, ContactMessage, Bike
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['bike', 'date']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class AdminSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['name', 'brand', 'price', 'image', 'description']
