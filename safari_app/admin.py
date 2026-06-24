from django.contrib import admin
from .models import HabitatZone, Animal, TourGuide, Booking, GalleryImage, SiteSettings, ContactMessage

admin.site.register(HabitatZone)
admin.site.register(Animal)
admin.site.register(TourGuide)
admin.site.register(Booking)
admin.site.register(GalleryImage)
admin.site.register(SiteSettings)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    readonly_fields = ('name', 'email', 'message', 'submitted_at')
