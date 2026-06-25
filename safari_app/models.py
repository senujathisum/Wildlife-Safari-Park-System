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
    profile_image = models.URLField(max_length=500, default='https://static.vecteezy.com/system/resources/previews/036/190/419/original/business-man-blank-profile-image-with-beard-vector.jpg')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    TIER_CHOICES = [
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    guest_name = models.CharField(max_length=100)
    contact_email = models.EmailField(default='guest@example.com')
    contact_phone = models.CharField(max_length=20, default='0000000000')
    number_of_guests = models.PositiveIntegerField(default=1)
    booking_date = models.DateField()
    slot_time = models.TimeField()
    pricing_tier = models.CharField(max_length=20, choices=TIER_CHOICES, default='Standard')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    # Admin Assigned Fields
    vehicle_number = models.CharField(max_length=20, blank=True, null=True)
    assigned_guide = models.ForeignKey(TourGuide, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')

    def __str__(self):
        return f"Booking for {self.guest_name} on {self.booking_date} ({self.status})"

class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField()

    def __str__(self):
        return self.title

class SiteSettings(models.Model):
    logo_url = models.URLField(max_length=500, blank=True, null=True, help_text="URL for the site logo")

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name_plural = "Site Settings"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
