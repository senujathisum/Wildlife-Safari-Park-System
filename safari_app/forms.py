from django import forms
from .models import Booking
import datetime

class BookingForm(forms.ModelForm):
    booking_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.date.today().strftime('%Y-%m-%d'), 'class': 'form-control'})
    )
    slot_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})
    )

    class Meta:
        model = Booking
        fields = ['guest_name', 'contact_email', 'contact_phone', 'number_of_guests', 'booking_date', 'slot_time', 'pricing_tier']
        widgets = {
            'guest_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '10'}),
            'pricing_tier': forms.Select(attrs={'class': 'form-control'}),
        }
