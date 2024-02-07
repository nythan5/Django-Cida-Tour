from django.contrib import admin
from .models import Customer, Trip, Category, TripCustomer, Payment

# Register your models here.
admin.site.register(Category),
admin.site.register(Trip),
admin.site.register(Customer),
admin.site.register(TripCustomer),
admin.site.register(Payment),
