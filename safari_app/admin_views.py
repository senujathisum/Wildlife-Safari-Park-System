from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Booking, TourGuide, HabitatZone, Animal, GalleryImage, SiteSettings, ContactMessage
from django.contrib import messages

# Mixin for auth
class StaffRequiredMixin(UserPassesTestMixin):
    login_url = reverse_lazy('admin:login')

    def test_func(self):
        return self.request.user.is_staff

@user_passes_test(lambda u: u.is_staff, login_url='admin:login')
def dashboard_home(request):
    context = {
        'recent_bookings': Booking.objects.order_by('-id')[:5],
        'pending_bookings_count': Booking.objects.filter(status='Pending').count(),
        'active_guides_count': TourGuide.objects.filter(status='Active').count(),
        'unread_messages_count': ContactMessage.objects.count() # simplified
    }
    return render(request, 'dashboard/home.html', context)

# --- Bookings ---
class BookingListView(StaffRequiredMixin, ListView):
    model = Booking
    template_name = 'dashboard/booking_list.html'
    context_object_name = 'bookings'
    ordering = ['-booking_date', 'slot_time']

class BookingUpdateView(StaffRequiredMixin, UpdateView):
    model = Booking
    template_name = 'dashboard/generic_form.html'
    fields = ['status', 'vehicle_number', 'assigned_guide']
    success_url = reverse_lazy('safari_app:dashboard_bookings')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Booking'
        return context

# --- Tour Guides ---
class TourGuideListView(StaffRequiredMixin, ListView):
    model = TourGuide
    template_name = 'dashboard/guide_list.html'
    context_object_name = 'guides'

class TourGuideCreateView(StaffRequiredMixin, CreateView):
    model = TourGuide
    template_name = 'dashboard/generic_form.html'
    fields = '__all__'
    success_url = reverse_lazy('safari_app:dashboard_guides')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Tour Guide'
        return context

class TourGuideUpdateView(StaffRequiredMixin, UpdateView):
    model = TourGuide
    template_name = 'dashboard/generic_form.html'
    fields = '__all__'
    success_url = reverse_lazy('safari_app:dashboard_guides')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Tour Guide'
        return context

class TourGuideDeleteView(StaffRequiredMixin, DeleteView):
    model = TourGuide
    template_name = 'dashboard/generic_confirm_delete.html'
    success_url = reverse_lazy('safari_app:dashboard_guides')

# --- Habitat Zones ---
class HabitatZoneListView(StaffRequiredMixin, ListView):
    model = HabitatZone
    template_name = 'dashboard/habitat_list.html'
    context_object_name = 'habitats'

class HabitatZoneCreateView(StaffRequiredMixin, CreateView):
    model = HabitatZone
    template_name = 'dashboard/generic_form.html'
    fields = '__all__'
    success_url = reverse_lazy('safari_app:dashboard_habitats')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Habitat Zone'
        return context

class HabitatZoneUpdateView(StaffRequiredMixin, UpdateView):
    model = HabitatZone
    template_name = 'dashboard/generic_form.html'
    fields = '__all__'
    success_url = reverse_lazy('safari_app:dashboard_habitats')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Habitat Zone'
        return context

# --- Animals ---
class AnimalListView(StaffRequiredMixin, ListView):
    model = Animal
    template_name = 'dashboard/animal_list.html'
    context_object_name = 'animals'

class AnimalCreateView(StaffRequiredMixin, CreateView):
    model = Animal
    template_name = 'dashboard/generic_form.html'
    fields = ['species', 'health_status', 'habitat']
    success_url = reverse_lazy('safari_app:dashboard_animals')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Animal'
        return context

class AnimalUpdateView(StaffRequiredMixin, UpdateView):
    model = Animal
    template_name = 'dashboard/generic_form.html'
    fields = ['species', 'health_status', 'habitat']
    success_url = reverse_lazy('safari_app:dashboard_animals')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Animal'
        return context

# --- Gallery Images ---
class GalleryImageListView(StaffRequiredMixin, ListView):
    model = GalleryImage
    template_name = 'dashboard/gallery_list.html'
    context_object_name = 'images'

class GalleryImageCreateView(StaffRequiredMixin, CreateView):
    model = GalleryImage
    template_name = 'dashboard/generic_form.html'
    fields = '__all__'
    success_url = reverse_lazy('safari_app:dashboard_gallery')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Gallery Image'
        return context

class GalleryImageUpdateView(StaffRequiredMixin, UpdateView):
    model = GalleryImage
    template_name = 'dashboard/generic_form.html'
    fields = '__all__'
    success_url = reverse_lazy('safari_app:dashboard_gallery')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Gallery Image'
        return context

class GalleryImageDeleteView(StaffRequiredMixin, DeleteView):
    model = GalleryImage
    template_name = 'dashboard/generic_confirm_delete.html'
    success_url = reverse_lazy('safari_app:dashboard_gallery')

# --- Contact Messages ---
class ContactMessageListView(StaffRequiredMixin, ListView):
    model = ContactMessage
    template_name = 'dashboard/message_list.html'
    context_object_name = 'messages_list'
    ordering = ['-submitted_at']

class ContactMessageDeleteView(StaffRequiredMixin, DeleteView):
    model = ContactMessage
    template_name = 'dashboard/generic_confirm_delete.html'
    success_url = reverse_lazy('safari_app:dashboard_messages')

# --- Site Settings ---
@user_passes_test(lambda u: u.is_staff, login_url='admin:login')
def site_settings_view(request):
    settings, created = SiteSettings.objects.get_or_create(id=1)
    if request.method == 'POST':
        settings.logo_url = request.POST.get('logo_url')
        settings.save()
        messages.success(request, 'Settings saved!')
        return redirect('safari_app:dashboard_settings')
    return render(request, 'dashboard/settings.html', {'settings': settings})
