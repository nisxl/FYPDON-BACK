from django.contrib import admin
from .models import Product
from .models import ShippingAddress
from .models import Note
# Register your models here.

admin.site.register(Note)
admin.site.register(Product)
admin.site.register(ShippingAddress)
