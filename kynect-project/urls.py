"""kynect-project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import kynect.views
from kynect.forms import LoginForm
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', kynect.views.home, name="home"),
	url(r'^home/', kynect.views.home),
    url(r'^help/', kynect.views.help),
    url(r'^team/', kynect.views.team),
    url(r'^contact_us/', kynect.views.contact_us),
    url(r'^testimonials/', kynect.views.testimonials),
    url(r'^purchase/', kynect.views.purchase),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name="login"),
    url(r'^logout/', views.logout, {'next_page': '/home'}),
    url(r'^profile/', kynect.views.profile),
    url(r'^notifications/', kynect.views.notifications),
    url(r'^account_settings/', kynect.views.account_settings),
    url(r'^sign_up/', kynect.views.sign_up),
]
