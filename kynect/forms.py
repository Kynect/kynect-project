from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.gis import forms as gisforms
from kynect.models import Location, Pet, User_Profile
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import PointField
from django.forms.widgets import DateInput, TextInput
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
import datetime

class PetDetailsForm(forms.ModelForm):
	def clean_name(self):
		data = self.cleaned_data['name']

		# DATA VALIDATION HERE:

		# Remember to always return the cleaned data.
		return data

	def clean_breed(self):
		data = self.cleaned_data['breed']

		# DATA VALIDATION HERE:

		# Remember to always return the cleaned data.
		return data

	def clean_dob(self):
		data = self.cleaned_data['dob']

		#Check date is not in past. 
		if data > datetime.date.today():
			raise ValidationError(_('Invalid date - Date must be in past or present.'), code='invalid')

		# Remember to always return the cleaned data.
		return data

	class Meta:
		model = Pet
		fields = ['name', 'breed', 'dob']
		labels = {
			"name": "Name",
			"breed": "Breed",
			"dob": "Date of Birth"
		}

class AccountDetailsForm(forms.ModelForm):
	def clean_phone(self):
		data = self.cleaned_data['phone']

		# DATA VALIDATION HERE:

		# Remember to always return the cleaned data.
		return data

	def clean_street(self):
		data = self.cleaned_data['street']

		# DATA VALIDATION HERE:

		# Remember to always return the cleaned data.
		return data

	def clean_apt(self):
		data = self.cleaned_data['apt']

		# DATA VALIDATION HERE:

		# Remember to always return the cleaned data.
		return data

	def clean_city(self):
		data = self.cleaned_data['city']

		# DATA VALIDATION HERE:

		# Remember to always return the cleaned data.
		return data

	def clean_state(self):
		data = self.cleaned_data['state']

		# DATA VALIDATION HERE:

		# Remember to always return the cleaned data.
		return data

	def clean_zip_code(self):
		data = self.cleaned_data['zip_code']

		# DATA VALIDATION HERE:

		# Remember to always return the cleaned data.
		return data
		
	class Meta:
		model = User_Profile
		fields = ['phone', 'street', 'apt', 'city', 'state', 'zip_code']
		labels = {
			"phone": "Phone",
			"street": "Street",
			"apt": "Apt",
			"city": "City",
			"state": "State",
			"zip_code": "Zip Code"
		}

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=100)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Password'}))

class CoordinateAdminEntryForm(gisforms.ModelForm):
	coordinates = gisforms.PointField(widget=gisforms.OSMWidget(attrs={'display_raw': True}))