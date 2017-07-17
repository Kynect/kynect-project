from django.contrib import admin

from .models import Owner
from .models import Owner_Address
from .models import Device_Type
from .models import Service_Plan
from .models import Device
from .models import Pet
from .models import Location

# Register your models here.
admin.site.register(Owner)
admin.site.register(Owner_Address)
admin.site.register(Device_Type)
admin.site.register(Service_Plan)
admin.site.register(Device)
admin.site.register(Pet)
admin.site.register(Location)
