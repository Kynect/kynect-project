from django.contrib.postgres.operations import CreateExtension
from django.db import migrations
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create database extensions here:

class Migration(migrations.Migration):
	operations = [
        CreateExtension('postgis'),
	]

# Create your models here:

class User_Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
	phone_regex = RegexValidator(regex=r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$', message="Phone Number Entered Incorrectly")
	phone = models.CharField(max_length=25, validators=[phone_regex], blank=True) # validators should be a list
	street = models.CharField(max_length=50)
	apt = models.CharField(max_length=20, blank=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=20)
	zip_code = models.CharField(max_length=16)
	email_confirmed = models.BooleanField(default=False)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		User_Profile.objects.create(user=instance)
	instance.user_profile.save()

class Device_Type(models.Model):
	version = models.CharField(max_length=10)
	size = models.CharField(max_length=15)
	color = models.CharField(max_length=15)

	def __str__(self):
		return str(self.id) + '_' + self.version + '_' + self.size + '_' + self.color

class Service_Plan(models.Model):
	data_limit = models.CharField(max_length=10)
	data_interval = models.CharField(max_length=10)
	cost_per_month = models.IntegerField()
	cost_per_year = models.IntegerField()

	def __str__(self):
		return str(self.id) + '_' + str(self.data_interval) + '_$' + str(self.cost_per_year)

class Device(models.Model):
	user_profile = models.ForeignKey(User_Profile, on_delete=models.CASCADE, related_name='devices')
	device_type = models.ForeignKey(Device_Type, on_delete=models.PROTECT, related_name='devices')
	service_plan = models.ForeignKey(Service_Plan, on_delete=models.PROTECT, related_name='devices')
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.id) + '_' + self.user_profile.user.username

class Pet(models.Model):
	user_profile = models.ForeignKey(User_Profile, on_delete=models.CASCADE, related_name='pets')
	device = models.OneToOneField(Device, on_delete=models.PROTECT, related_name='pet')
	name = models.CharField(max_length=30)
	breed = models.CharField(max_length=35)
	dob = models.DateField()
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.id) + '_' + self.name

class Geofence(models.Model):
	pet = models.OneToOneField(Pet, on_delete=models.CASCADE, related_name='geofence')
	latitude = models.DecimalField(max_digits=10, decimal_places=6)
	longitude = models.DecimalField(max_digits=10, decimal_places=6)
	coordinates = models.PointField(srid=4326)
	objects = models.GeoManager()
	radius = models.IntegerField()
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.pet.name + '_' + str(self.id)

class Location(models.Model):
	pet = models.OneToOneField(Pet, on_delete=models.CASCADE, related_name='location')
	latitude = models.DecimalField(max_digits=10, decimal_places=6)
	longitude = models.DecimalField(max_digits=10, decimal_places=6)
	coordinates = models.PointField(geography=True, srid=4326)
	objects = models.GeoManager()
	alt = models.DecimalField(max_digits=5, decimal_places=1, default=0000.0)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.pet.name + '_' + str(self.id)
