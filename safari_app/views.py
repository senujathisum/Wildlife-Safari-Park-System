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

def contact_us(request):
    from .models import ContactMessage
    from django.contrib import messages
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'contact.html')
