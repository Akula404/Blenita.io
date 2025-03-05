from django.contrib import admin
from .models import TableBooking, Contact, Menu, Special, Event, Gallery, Chef, Testimonial, Order

@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'people', 'message')
    search_fields = ('name', 'email', 'phone', 'date')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject')

admin.site.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'price', 'img')
    search_fields = ('name', 'desc', 'price')

admin.site.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'info', 'img')

admin.site.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'desc', 'img', 'offer')

admin.site.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('img')

admin.site.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'img')

admin.site.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'desc', 'img')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'contact_number', 'item_name', 'quantity', 'item_price', 'total_price', 'order_date')
    list_filter = ('order_date',)
    search_fields = ('customer_name', 'contact_number', 'item_name')
    ordering = ('-order_date',)