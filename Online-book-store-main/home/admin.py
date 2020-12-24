from django.contrib import admin

# Register your models here.
from .models import Book, Order, OrderUpdate

admin.site.register(Book)
admin.site.register(Order)
admin.site.register(OrderUpdate)

