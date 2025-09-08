"""from django.contrib import admin
from .models import Bike
# Register your models here.

admin.site.register(Bike)"""

# bike/admin.py
"""from django.contrib import admin
from .models import Bike

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('brand','name','price')
    search_fields = ('brand','name')"""

# bike/admin.py
from django.contrib import admin
from .models import AdminProfile, Bike, Booking, ContactMessage

admin.site.register(AdminProfile)
admin.site.register(Bike)
admin.site.register(Booking)
admin.site.register(ContactMessage)



