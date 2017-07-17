from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations

# Create database extensions here:

class Migration(migrations.Migration):
	operations = [
        CreateExtension('postgis'),
	]

# Create your models here:

class Owner(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_regex = RegexValidator(regex=r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$', message="Phone Number Entered Incorrectly")
	phone_number = models.CharField(max_length=25, validators=[phone_regex], blank=True) # validators should be a list
	verified = models.BooleanField(default=False)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.username

class Owner_Address(models.Model):
	owner = models.OneToOneField(Owner, on_delete=models.CASCADE)
	street = models.CharField(max_length=50, blank=False, null=False)
	apt = models.CharField(max_length=20, null=True, blank=True)
	city = models.CharField(max_length=50, blank=False, null=False)
	zip_code = models.CharField(max_length=16, blank=False, null=False)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.street + ', ' + self.city + ', ' + self.zip_code

class Device_Type(models.Model):
	version = models.CharField(max_length=10, blank=False, null=False)
	size = models.CharField(max_length=15, blank=False, null=False)
	color = models.CharField(max_length=15, blank=False, null=False)

	def __str__(self):
		return self.id + '_' + self.version + '_' + self.size + '_' + self.color

class Service_Plan(models.Model):
	data_limit = models.CharField(max_length=10, blank=False, null=False)
	data_interval = models.CharField(max_length=10, blank=False, null=False)
	cost_per_month = models.IntegerField(blank=False, null=False)
	cost_per_year = models.IntegerField(blank=False, null=False)

	def __str__(self):
		return self.id + '_' + self.data_interval + '_' + self.cost_per_month

class Device(models.Model):
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
	device_type = models.ForeignKey(Device_Type, on_delete=models.PROTECT, null=True)
	service_plan = models.ForeignKey(Service_Plan, on_delete=models.PROTECT, null=True)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.id + '_' + self.owner.user.username

class Pet(models.Model):
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
	device = models.OneToOneField(Device, on_delete=models.PROTECT)
	name = models.CharField(max_length=30, blank=False, null=False)
	breed = models.CharField(max_length=35, blank=False, null=False)
	dob = models.DateField(blank=False, null=False)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.id + '_' + self.name

# class Geofence(models.Model):


class Location(models.Model):
	device = models.ForeignKey(Device, on_delete=models.CASCADE)
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=False, null=True)
	lat = models.DecimalField(max_digits=9, decimal_places=6, blank=False, null=True)
	lng = models.DecimalField(max_digits=9, decimal_places=6, blank=False, null=True)
	alt = models.DecimalField(max_digits=5, decimal_places=1, default=0.0, blank=False, null=True)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.device.name + '_' + self.id
