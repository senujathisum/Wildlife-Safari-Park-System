from django.urls import path
from . import views, admin_views

app_name = 'safari_app'

urlpatterns = [
    path('packages/', views.packages, name='packages'),
    path('book-now/', views.book_now, name='book_now'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('guides/', views.guides_list, name='guides'),
    path('habitats/', views.habitats_list, name='habitats'),
    path('contact/', views.contact_us, name='contact'),

    # Dashboard URLs
    path('dashboard/', admin_views.dashboard_home, name='dashboard_home'),
    path('dashboard/bookings/', admin_views.BookingListView.as_view(), name='dashboard_bookings'),
    path('dashboard/bookings/<int:pk>/edit/', admin_views.BookingUpdateView.as_view(), name='dashboard_booking_edit'),
    path('dashboard/guides/', admin_views.TourGuideListView.as_view(), name='dashboard_guides'),
    path('dashboard/guides/add/', admin_views.TourGuideCreateView.as_view(), name='dashboard_guide_add'),
    path('dashboard/guides/<int:pk>/edit/', admin_views.TourGuideUpdateView.as_view(), name='dashboard_guide_edit'),
    path('dashboard/guides/<int:pk>/delete/', admin_views.TourGuideDeleteView.as_view(), name='dashboard_guide_delete'),
    path('dashboard/habitats/', admin_views.HabitatZoneListView.as_view(), name='dashboard_habitats'),
    path('dashboard/habitats/add/', admin_views.HabitatZoneCreateView.as_view(), name='dashboard_habitat_add'),
    path('dashboard/habitats/<int:pk>/edit/', admin_views.HabitatZoneUpdateView.as_view(), name='dashboard_habitat_edit'),
    path('dashboard/animals/', admin_views.AnimalListView.as_view(), name='dashboard_animals'),
    path('dashboard/animals/add/', admin_views.AnimalCreateView.as_view(), name='dashboard_animal_add'),
    path('dashboard/animals/<int:pk>/edit/', admin_views.AnimalUpdateView.as_view(), name='dashboard_animal_edit'),
    path('dashboard/gallery/', admin_views.GalleryImageListView.as_view(), name='dashboard_gallery'),
    path('dashboard/gallery/add/', admin_views.GalleryImageCreateView.as_view(), name='dashboard_gallery_add'),
    path('dashboard/gallery/<int:pk>/edit/', admin_views.GalleryImageUpdateView.as_view(), name='dashboard_gallery_edit'),
    path('dashboard/gallery/<int:pk>/delete/', admin_views.GalleryImageDeleteView.as_view(), name='dashboard_gallery_delete'),
    path('dashboard/messages/', admin_views.ContactMessageListView.as_view(), name='dashboard_messages'),
    path('dashboard/messages/<int:pk>/delete/', admin_views.ContactMessageDeleteView.as_view(), name='dashboard_message_delete'),
    path('dashboard/settings/', admin_views.site_settings_view, name='dashboard_settings'),
]
