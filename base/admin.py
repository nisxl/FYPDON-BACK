from django.contrib import admin
from .models import *
from .models import Note
# Register your models here.

admin.site.register(Note)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
