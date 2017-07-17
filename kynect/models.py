from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations
from django.contrib.gis.geos import Point
from django.contrib.gis.db import models as geomodels

# Create database extensions here:

class Migration(migrations.Migration):
	operations = [
        CreateExtension('postgis'),
	]

# Create your models here:

class Owner(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_regex = RegexValidator(regex=r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$', message="Phone Number Entered Incorrectly")
	phone_number = models.CharField(max_length=25, validators=[phone_regex]) # validators should be a list
	verified = models.BooleanField(default=False)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.username

class Owner_Address(models.Model):
	owner = models.OneToOneField(Owner, on_delete=models.CASCADE)
	street = models.CharField(max_length=50)
	apt = models.CharField(max_length=20, blank=True)
	city = models.CharField(max_length=50)
	zip_code = models.CharField(max_length=16)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.street + ', ' + self.city + ', ' + self.zip_code

class Device_Type(models.Model):
	version = models.CharField(max_length=10)
	size = models.CharField(max_length=15)
	color = models.CharField(max_length=15)

	def __str__(self):
		return self.id + '_' + self.version + '_' + self.size + '_' + self.color

class Service_Plan(models.Model):
	data_limit = models.CharField(max_length=10)
	data_interval = models.CharField(max_length=10)
	cost_per_month = models.IntegerField()
	cost_per_year = models.IntegerField()

	def __str__(self):
		return self.id + '_' + self.data_interval + '_' + self.cost_per_month

class Device(models.Model):
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
	device_type = models.ForeignKey(Device_Type, on_delete=models.PROTECT)
	service_plan = models.ForeignKey(Service_Plan, on_delete=models.PROTECT)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.id + '_' + self.owner.user.username

class Pet(models.Model):
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
	device = models.OneToOneField(Device, on_delete=models.PROTECT)
	name = models.CharField(max_length=30)
	breed = models.CharField(max_length=35)
	dob = models.DateField()
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.id + '_' + self.name

class Geofence(models.Model):
	pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
	center = geomodels.PointField(srid=4326)
	radius = models.IntegerField()
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.id + '_' + self.pet.name


class Location(models.Model):
	device = models.ForeignKey(Device, on_delete=models.CASCADE)
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
	point = geomodels.PointField(srid=4326)
	alt = models.DecimalField(max_digits=5, decimal_places=1, default=0000.0)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.device.name + '_' + self.id
