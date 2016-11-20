from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Device(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, default='Hawki')
	IMEI = models.CharField(max_length=15, blank=False, null=False)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class Location(models.Model):
	device = models.ForeignKey(Device, on_delete=models.CASCADE)
	lat = models.DecimalField(max_digits=13, decimal_places=10, default=0.0000000000)
	lng = models.DecimalField(max_digits=13, decimal_places=10, default=0.0000000000)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.device.name + '_' + str(self.id)
