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

    path('place_order/', views.place_order, name='place_order'),
    path('order_success/', views.order_success, name='order_success'),

    path('show_order/', views.show_order, name='show_order'),
    path('edit_order/<int:order_id>/', views.edit_order, name='edit_order'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),

    
]
