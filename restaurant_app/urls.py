from django.urls import path
from .import views

app_name = 'restaurant_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chef/', views.chef, name='chef'),
    path('book_a_table/', views.book_a_table, name='book_a_table'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('menu/', views.menu, name='menu'),
    path('specials/', views.specials, name='specials'),
    
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('update_contact/<int:contact_id>/', views.update_contact, name='update_contact'),
    path('contact/<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('show_contact/', views.show_contact, name='show_contact'),
    
    path('show_book_a_table/', views.show_book_a_table, name='show_book_a_table'),
    
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('update_booking/<int:booking_id>/', views.update_booking, name='update_booking'),

    
]
