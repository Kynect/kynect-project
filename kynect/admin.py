from django.contrib.gis import admin
from kynect.models import User_Profile
from kynect.models import Device_Type
from kynect.models import Service_Plan
from kynect.models import Device
from kynect.models import Pet
from kynect.models import Geofence
from kynect.models import Location
from kynect.forms import CoordinateAdminEntryForm

class CoordinateAdminEntry(admin.GeoModelAdmin):
    form = CoordinateAdminEntryForm

# Register your models here.
admin.site.register(User_Profile)
admin.site.register(Device_Type)
admin.site.register(Service_Plan)
admin.site.register(Device)
admin.site.register(Pet)
admin.site.register(Geofence, CoordinateAdminEntry)
admin.site.register(Location, CoordinateAdminEntry)
