from django.urls import path
from . import views

app_name = 'safari_app'

urlpatterns = [
    path('bookings/', views.bookings_list, name='bookings'),
    path('guides/', views.guides_list, name='guides'),
    path('habitats/', views.habitats_list, name='habitats'),
    path('contact/', views.contact_us, name='contact'),
]
