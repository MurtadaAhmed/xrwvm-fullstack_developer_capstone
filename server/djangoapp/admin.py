from django.contrib import admin
from .models import CarMake, CarModel

# Allows adding CarModels directly when editing a CarMake in the admin dashboard
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of empty model forms to show by default

# Admin configuration for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')
    search_fields = ['name']

# Admin configuration for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')
    list_filter = ['type', 'car_make', 'year']
    search_fields = ['name', 'car_make__name']

# Registering models with their customized admin classes
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)