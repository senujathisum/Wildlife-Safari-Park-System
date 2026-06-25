from django.urls import path
from . import views

app_name = 'safari_app'

urlpatterns = [
    path('packages/', views.packages, name='packages'),
    path('book-now/', views.book_now, name='book_now'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('guides/', views.guides_list, name='guides'),
    path('habitats/', views.habitats_list, name='habitats'),
    path('contact/', views.contact_us, name='contact'),
]
