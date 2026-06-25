from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking, TourGuide, HabitatZone, GalleryImage
from .forms import BookingForm

def index(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'index.html', {'gallery_images': gallery_images})

def packages(request):
    return render(request, 'packages.html')

def book_now(request):
    initial_tier = request.GET.get('tier', 'Standard')
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('safari_app:booking_success')
    else:
        form = BookingForm(initial={'pricing_tier': initial_tier})
    
    return render(request, 'book_now.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')

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
