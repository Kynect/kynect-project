from django.contrib import admin
from kynect.models import Owner, Owner_Address, Device_Type, Service_Plan, Device, Pet, Geofence, Location
from django.contrib.gis import admin
from django.contrib.gis import forms
from django.contrib.gis.db import models 

class LocationAdminForm(forms.ModelForm):
    point = forms.PointField(widget=forms.OSMWidget(attrs={
            'display_raw': True}))

class LocationAdmin(admin.GeoModelAdmin):
    form = LocationAdminForm

# Register your models here.
admin.site.register(Owner)
admin.site.register(Owner_Address)
admin.site.register(Device_Type)
admin.site.register(Service_Plan)
admin.site.register(Device)
admin.site.register(Pet)
admin.site.register(Geofence)
admin.site.register(Location, LocationAdmin)