from django.contrib import admin

from .models import Device
from .models import Location

# Register your models here.
admin.site.register(Device)
admin.site.register(Location)
