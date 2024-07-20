from django.contrib import admin
from .models import cart, cartItem

# Register your models here.
admin.site.register(cartItem)
admin.site.register(cart)