from django.contrib import admin
from .models import product

# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ('name','slug', 'price', 'stock', 'is_available','created_date')
    list_display_links = ['name', 'slug']
    readonly_fields = ('created_date', 'modified_date')
    prepopulated_fields = { 'slug' :('name',) }

admin.site.register(product,productAdmin)