from django.shortcuts import render
from .models import Booking, TourGuide, HabitatZone, GalleryImage

def index(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'index.html', {'gallery_images': gallery_images})

def bookings_list(request):
    bookings = Booking.objects.all().order_by('booking_date', 'slot_time')
    return render(request, 'bookings.html', {'bookings': bookings})

def guides_list(request):
    guides = TourGuide.objects.all().prefetch_related('assigned_zones')
    return render(request, 'guides.html', {'guides': guides})

def habitats_list(request):
    habitats = HabitatZone.objects.all().prefetch_related('animals')
    return render(request, 'habitats.html', {'habitats': habitats})
