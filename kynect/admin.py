from django.contrib.gis import admin
from django.conf import settings
from kynect.models import User_Profile
from kynect.models import Device_Type
from kynect.models import Service_Plan
from kynect.models import Device
from kynect.models import Pet
from kynect.models import Geofence
from kynect.models import Location
from kynect.forms import CoordinateAdminEntryForm

class GeofenceAdmin(admin.GeoModelAdmin):
	form = CoordinateAdminEntryForm

	fieldsets = (
		(None, {
			'fields': ('pet', 'latitude', 'longitude','coordinates', 'radius', 'date_added')
		}),
	)

	class Media:
		if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
			css = {
				'all': ('css/admin/location_picker.css',),
			}
			js = (
				'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
				'js/admin/location_picker.js',
			)

class LocationAdmin(admin.GeoModelAdmin):
	form = CoordinateAdminEntryForm

	fieldsets = (
		(None, {
			'fields': ('pet', 'latitude', 'longitude','coordinates', 'alt', 'date_added')
		}),
	)

	class Media:
		if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
			css = {
				'all': ('css/admin/location_picker.css',),
			}
			js = (
				'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
				'js/admin/location_picker.js',
			)

# Register your models here.
admin.site.register(User_Profile)
admin.site.register(Device_Type)
admin.site.register(Service_Plan)
admin.site.register(Device)
admin.site.register(Pet)
admin.site.register(Geofence, GeofenceAdmin)
admin.site.register(Location, LocationAdmin)
