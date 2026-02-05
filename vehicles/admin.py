from django.contrib import admin
from .models import Brand, Vehicle

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin_country', 'is_active', 'created_at')
    search_fields = ('name','origin_country')

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model_name','year', 'vin', 'colour', 'created_by', 'created_at', 'updated_at')
    list_filter = ('brand', 'year', 'colour')
    search_fields = ('vin', 'model_name')

admin.site.register(Brand, BrandAdmin)
admin.site.register(Vehicle, VehicleAdmin)
# Register your models here.
