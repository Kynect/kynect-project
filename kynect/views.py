from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from kynect.forms import SignUpForm, PetDetailsForm, AccountDetailsForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from kynect.tokens import account_activation_token
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User_Profile, Device, Pet, Notification


def home(request):
	return render(request, 'index.html')

def how_it_works(request):
	return render(request, 'how_it_works.html')

def features(request):
	return render(request, 'features.html')

def about_us(request):
	return render(request, 'about_us.html')

def subscribe(request):
	return render(request, 'subscribe.html')

def account_portal(request):
	return render(request, 'account/account_portal.html')

def user_devices(request):
	if not request.user.is_authenticated():
		return redirect('/home')

	current_user = request.user
	devices = current_user.devices.all()

	context = {
		# include contexts for here
		'user': current_user,
		'devices': devices, 			
	}

	return render(request, 'account/user_devices.html', context)

def track_location(request):
	if not request.user.is_authenticated():
		return redirect('/home')

	current_user = request.user
	devices = current_user.devices.all()

	context = {
		# include contexts for here
		'user': current_user,
		'devices': devices,						
	}

	return render(request, 'account/track_location.html', context)

@csrf_exempt
def update_location(request, device_id):
	if request.method == 'POST':
		device_instance = get_object_or_404(Device, id = device_id)

		post_data = request.body

		return HttpResponse('Post Data Received OK:\n' + str(post_data))
	else:
		return HttpResponse('No POST Received')

def pet_details(request):
	if not request.user.is_authenticated():
		return redirect('/home')

	current_user = request.user	
	devices = current_user.devices.all()									
	form = PetDetailsForm()

	context = {
		# include contexts for here
		'user': current_user,
		'devices': devices,
		'form': form,						
	}

	return render(request, 'account/pet_details.html', context)

def update_pet_details(request, pet_id):
	if not request.user.is_authenticated():
		return redirect('/home')

	pet_instance = get_object_or_404(Pet, id = pet_id)

	if request.method == 'POST':
		form = PetDetailsForm(request.POST)					# Create a form instance and populate it with data from the request (binding):

		if form.is_valid():
			user_admin = User.objects.get(username='Kynect')
			current_user = request.user
			devices = current_user.devices.all()
		
			context = {
				# include contexts for here
				'user': current_user,
				'devices': devices,
				'form': form,						
			}

			# store old pet information
			old_pet_name = pet_instance.name
			old_pet_breed = pet_instance.breed
			old_pet_dob = pet_instance.dob

			# process the data in form.cleaned_data as required (here we just write it to the model fields)
			pet_instance.name = form.cleaned_data['name']
			pet_instance.breed = form.cleaned_data['breed']
			pet_instance.dob = form.cleaned_data['dob']
			pet_instance.save()

			notification = Notification.objects.create(
				sender = user_admin,
				receiver = current_user,
				subject = 'Pet Details Change',
				content = 'Hello ' + current_user.first_name + ", you just recently changed your pet's details:\n" + 
							"Name: " + old_pet_name + " --> " + pet_instance.name + "\n" +
							"Breed: " + old_pet_breed + " --> " + pet_instance.breed + "\n" +
							"Date of Birth: " + str(old_pet_dob) + " --> " + str(pet_instance.dob)
			)

			notification.save()	

			return render(request, 'account/pet_details.html', context)
	else:
		current_user = request.user	
		devices = current_user.devices.all()
		form = PetDetailsForm()
			
		context = {
			# include contexts for here
			'user': current_user,
			'devices': devices,
			'form': form,						
		}

		return render(request, 'account/pet_details.html', context)

	current_user = request.user
	devices = current_user.devices.all()	
	form = PetDetailsForm()
		
	context = {
		# include contexts for here
		'user': current_user,
		'devices': devices,
		'form': form,						
	}

	return render(request, 'account/pet_details.html', context)

def pet_health(request):
	return render(request, 'account/pet_health.html')

def notifications(request):
	if not request.user.is_authenticated():
		return redirect('/home')

	current_user = request.user	
	user_admin = User.objects.get(username='Kynect')
	received_notifications = current_user.notifications_received.all()
	sent_notifications = current_user.notifications_sent.all()

	if current_user == user_admin:
		is_admin = True
	else:
		is_admin = False

	context = {
		# include contexts for here
		'user': current_user,
		'received_notifications': received_notifications,
		'sent_notifications': sent_notifications,
		'is_admin':	is_admin,					
	}

	return render(request, 'account/notifications.html', context)

def delete_notifications(request, notification_id):
	if not request.user.is_authenticated():
		return redirect('/home')

	notification_instance = get_object_or_404(Notification, id = notification_id)
	notification_instance.delete()

	current_user = request.user	
	received_notifications = current_user.notifications_received.all()
	sent = current_user.notifications_sent.all()

	context = {
		# include contexts for here
		'user': current_user,
		'received_notifications': received_notifications,			
	}

	return render(request, 'account/notifications.html', context)

def account_settings(request):
	if not request.user.is_authenticated():
		return redirect('/home')

	current_user = request.user	
	user_profile_form = AccountDetailsForm()
	password_change_form = PasswordChangeForm(request.user)

	context = {
		# include contexts for here
		'user': current_user,
		'user_profile_form': user_profile_form,	
		'password_change_form': password_change_form,					
	}

	return render(request, 'account/account_settings.html', context)

def update_user_profile(request):
	if not request.user.is_authenticated():
		return redirect('/home')

	if request.method == 'POST':
		user_profile_form = AccountDetailsForm(request.POST)					# Create a form instance and populate it with data from the request (binding):

		if user_profile_form.is_valid():
			current_user = request.user
			user_admin = User.objects.get(username='Kynect')
			user_profile_instance = User_Profile.objects.get(user=current_user)

			# store old pet information
			old_user_phone = current_user.user_profile.phone
			old_user_street = current_user.user_profile.street
			old_user_apt = current_user.user_profile.apt
			old_user_city = current_user.user_profile.city
			old_user_state = current_user.user_profile.state
			old_user_zip = current_user.user_profile.zip_code

			# process the data in form.cleaned_data as required (here we just write it to the model fields)
			user_profile_instance.phone = user_profile_form.cleaned_data['phone']
			user_profile_instance.street = user_profile_form.cleaned_data['street']
			user_profile_instance.apt = user_profile_form.cleaned_data['apt']
			user_profile_instance.city = user_profile_form.cleaned_data['city']
			user_profile_instance.state = user_profile_form.cleaned_data['state']
			user_profile_instance.zip_code = user_profile_form.cleaned_data['zip_code']
			user_profile_instance.save()

			notification = Notification.objects.create(
				sender = user_admin,
				receiver = current_user,
				subject = 'Account Settings Change',
				content = "Hello " + current_user.first_name + ", you just recently changed your account details:\n" + 
							"Phone: " + old_user_phone + " --> " + user_profile_instance.phone + "\n" +
							"Street: " + old_user_street + " --> " + user_profile_instance.street + "\n" +
							"Apt: " + old_user_apt + " --> " + user_profile_instance.apt + "\n" +
							"City: " + old_user_city + " --> " + user_profile_instance.city + "\n" +
							"State: " + old_user_state + " --> " + user_profile_instance.state + "\n" +
							"Zip Code: " + old_user_zip + " --> " + user_profile_instance.zip_code
			)

			notification.save()	

			password_change_form = PasswordChangeForm(request.user)

			context = {
				# include contexts for here
				'user': user_profile_instance.user,
				'user_profile_form': user_profile_form,
				'password_change_form': password_change_form,			
			}

			return render(request, 'account/account_settings.html', context)
	else:
		current_user = request.user	
		user_profile_form = AccountDetailsForm()
		password_change_form = PasswordChangeForm(request.user)
			
		context = {
			# include contexts for here
			'user': current_user,
			'user_profile_form': user_profile_form,
			'password_change_form': password_change_form,						
		}

		return render(request, 'account/account_settings.html', context)

	current_user = request.user	
	user_profile_form = AccountDetailsForm()
	password_change_form = PasswordChangeForm(request.user)

	context = {
		# include contexts for here
		'user': current_user,
		'user_profile_form': user_profile_form,		
		'password_change_form': password_change_form,				
	}

	return render(request, 'account/account_settings.html', context)

def change_password(request):
	if not request.user.is_authenticated():
		return redirect('/home')

	if request.method == 'POST':
		password_change_form = PasswordChangeForm(request.user, request.POST)

		if password_change_form.is_valid():
			password_change_form.save()
			update_session_auth_hash(request, password_change_form.user)  # Important!
			messages.success(request, 'Your password was successfully updated!')

			user_admin = User.objects.get(username='Kynect')
			current_user = request.user

			notification = Notification.objects.create(
				sender = user_admin,
				receiver = current_user,
				subject = 'Password Change',
				content = "Hello " + current_user.first_name + ", you just recently changed your password!" 
			)

			notification.save()	

			return redirect('change_password')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		password_change_form = PasswordChangeForm(request.user)

	current_user = request.user	
	user_profile_form = AccountDetailsForm()

	context = {
		'user': current_user,
		'user_profile_form': user_profile_form,	
		'password_change_form': password_change_form,
	}

	return render(request, 'account/account_settings.html', context)

# def password_reset(request):																	# Implement these when auth.views is not being used
# 	return render(request, 'password_reset/password_reset_form.html')

# def password_reset_sent(request):
# 	return render(request, 'password_reset/password_reset_sent.html')

# def password_reset_confirm(request):
# 	return render(request, 'password_reset/password_reset_confirm.html')

def password_reset_complete(request):
	return render(request, 'password_reset/password_reset_complete.html')

# USE THIS SIGNUP VIEW FOR EMAIL CONFIRMATION INCLUDED
def sign_up(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			subject = 'Kynect Account Activation'
			message = render_to_string('account_activation/account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
			})
			user.email_user(subject, message)

			return redirect('account_activation_sent')
	else:
		current_user = request.user
		form = SignUpForm()

		context = {
			'user': current_user,
			'form': form,						
		}

		return render(request, 'registration_and_login/sign_up.html', context)

	current_user = request.user
	form = SignUpForm()

	context = {
		'user': current_user,
		'form': form,						
	}

	return render(request, 'registration_and_login/sign_up.html', context)

def account_activation_sent(request):
	return render(request, 'account_activation/account_activation_sent.html')

def activate_account(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.user_profile.email_confirmed = True
		user.save()
		login(request, user)

		return render(request, 'account_activation/account_activation_success.html')
	else:
		return render(request, 'account_activation/account_activation_invalid.html')
