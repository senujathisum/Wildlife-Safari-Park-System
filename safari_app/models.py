from django.db import models

class HabitatZone(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Animal(models.Model):
    species = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True, null=True)
    health_status = models.CharField(max_length=50, default='Healthy')
    habitat = models.ForeignKey(HabitatZone, on_delete=models.CASCADE, related_name='animals')

    def __str__(self):
        return f"{self.species} - {self.name}" if self.name else self.species

class TourGuide(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('On Leave', 'On Leave')], default='Active')
    assigned_zones = models.ManyToManyField(HabitatZone, related_name='guides')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    TIER_CHOICES = [
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    ]
    guest_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    slot_time = models.TimeField()
    vehicle_number = models.CharField(max_length=20)
    pricing_tier = models.CharField(max_length=20, choices=TIER_CHOICES, default='Standard')
    assigned_guide = models.ForeignKey(TourGuide, on_delete=models.SET_NULL, null=True, related_name='bookings')

    def __str__(self):
        return f"Booking for {self.guest_name} on {self.booking_date}"

class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField()

    def __str__(self):
        return self.title
