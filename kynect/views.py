from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from kynect.forms import SignUpForm, PetDetailsForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from kynect.tokens import account_activation_token

from .models import Device, Pet


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
	return render(request, 'account_portal.html')

def pet_health(request):
	return render(request, 'pet_health.html')

def track_location(request):
	if not request.user.is_authenticated():
		return redirect('/home')

	current_user = request.user
	pets = current_user.user_profile.pets.all()

	context = {
		# include contexts for here
		'user': current_user,
		'pets': pets,						
	}

	return render(request, 'track_location.html', context)

def user_devices(request):
	if not request.user.is_authenticated():
		return redirect('/home')

	current_user = request.user
	devices = current_user.user_profile.devices.all()

	context = {
		# include contexts for here
		'user': current_user,
		'devices': devices, 			
	}

	return render(request, 'user_devices.html', context)

def pet_details(request):
	if not request.user.is_authenticated():
		return redirect('/home')

	current_user = request.user	
	pets = current_user.user_profile.pets.all()									
	form = PetDetailsForm()

	context = {
		# include contexts for here
		'user': current_user,
		'pets': pets,
		'form': form,						
	}

	return render(request, 'pet_details.html', context)

def update_pet_details(request, pet_id):
	if not request.user.is_authenticated():
		return redirect('/home')

	pet_instance = get_object_or_404(Pet, id = pet_id)

	if request.method == 'POST':
		form = PetDetailsForm(request.POST)					# Create a form instance and populate it with data from the request (binding):

		if form.is_valid():
			# process the data in form.cleaned_data as required (here we just write it to the model fields)
			pet_instance.name = form.cleaned_data['name']
			pet_instance.breed = form.cleaned_data['breed']
			pet_instance.dob = form.cleaned_data['dob']
			pet_instance.save()

			current_user = request.user
			pets = current_user.user_profile.pets.all()	
		
			context = {
				# include contexts for here
				'user': current_user,
				'pets': pets,
				'form': form,						
			}

			return render(request, 'pet_details.html', context)
	else:
		current_user = request.user	
		pets = current_user.user_profile.pets.all()
		form = PetDetailsForm()
			
		context = {
			# include contexts for here
			'user': current_user,
			'pets': pets,
			'form': form,						
		}

		return render(request, 'pet_details.html', context)

	current_user = request.user
	pets = current_user.user_profile.pets.all()	
	form = PetDetailsForm(request.POST)
		
	context = {
		# include contexts for here
		'user': current_user,
		'pets': pets,
		'form': form,						
	}

	return render(request, 'pet_details.html', context)

def user_log(request):
	return render(request, 'user_log.html')

def account_settings(request):
	return render(request, 'account_settings.html')

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
			message = render_to_string('account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
			})
			user.email_user(subject, message)

			return redirect('account_activation_sent')
	else:
		form = SignUpForm()

		context = {
			'user': current_user,
			'form': form,						
		}
	return render(request, 'sign_up.html', context)

# USE THIS SIGNUP VIEW FOR NO EMAIL CONFIRMATION INCLUDED
# def sign_up(request):
# 	if request.method == 'POST':
# 		form = SignUpForm(request.POST)
		
# 		if form.is_valid():
# 			form.save()
# 			# user.refresh_from_db()  # load the profile instance created by the signal
# 			# user.profile.birth_date = form.cleaned_data.get('birth_date')					#Use these 3 Lines if you want to put extra fields (Birth Date) in Signup Form)
# 			# user.save()
# 			username = form.cleaned_data.get('username')
# 			raw_password = form.cleaned_data.get('password1')
# 			user = authenticate(username=username, password=raw_password)
# 			login(request, user)
			
# 			return redirect('home')
# 	else:
# 		form = SignUpForm()
# 	return render(request, 'sign_up.html', {'form': form})

def account_activation_sent(request):
	return render(request, 'account_activation_sent.html')

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

		return render(request, 'account_activation_success.html')
	else:
		return render(request, 'account_activation_invalid.html')

# *** IMPLEMENT BELOW WHEN BACK END IS BEING SET UP ***

# def profile(request):
# 	if not request.user.is_authenticated():
# 		return redirect('/home')

# 	current_user = request.user

# 	context = {
# 		# include contexts here
# 	}

# 	return render(request, 'profile.html', context)

# def notifications(request):
# 	if not request.user.is_authenticated():
# 		return redirect('/home')

# 	current_user = request.user

# 	context = {
# 		# include contexts here
# 	}

# 	return render(request, 'notifications.html', context)

# def account_settings(request):
# 	if not request.user.is_authenticated():
# 		return redirect('/home')

# 	current_user = request.user

# 	context = {
# 		# include contexts here
# 	}

# 	return render(request, 'account_settings.html', context)
