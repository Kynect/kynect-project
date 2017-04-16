from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User

from .models import Device


def home(request):
	current_user = request.user
	# device = Device.objects.get(pk=1)
	# deviceLocations = device.location_set.all()

	context = {
		# 'device': device,
		# 'deviceLocations': deviceLocations
	}

	return render(request, 'index.html', context)

def how_it_works(request):
	return render(request, 'how_it_works.html')

def features(request):
	return render(request, 'features.html')

def about_us(request):
	return render(request, 'about_us.html')

def FAQ(request):
	return render(request, 'FAQ.html')

def subscribe(request):
	return render(request, 'subscribe.html')

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
