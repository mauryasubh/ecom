from django.contrib import admin
from . models import category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):  
    list_filter = ["name"]
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug','desc']


admin.site.register(category,CategoryAdmin)