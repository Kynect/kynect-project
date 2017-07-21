from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from kynect.forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from kynect.tokens import account_activation_token

from .models import Device


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

def profile(request):
	return render(request, 'profile.html')

def track_location(request):
	return render(request, 'track_location.html')

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
	return render(request, 'sign_up.html', {'form': form})

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
