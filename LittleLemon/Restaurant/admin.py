from django.contrib import admin

from LittleLemon.Restaurant.models import Menu
from LittleLemon.Restaurant.models import Booking

# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)