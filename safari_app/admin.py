from django.contrib import admin
from .models import HabitatZone, Animal, TourGuide, Booking, GalleryImage, SiteSettings

admin.site.register(HabitatZone)
admin.site.register(Animal)
admin.site.register(TourGuide)
admin.site.register(Booking)
admin.site.register(GalleryImage)
admin.site.register(SiteSettings)
