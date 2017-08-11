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

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
import kynect.views
from kynect.forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', kynect.views.home, name="home"),
    url(r'^home/', kynect.views.home),
    url(r'^features/', kynect.views.features),
    url(r'^about_us/', kynect.views.about_us),
    url(r'^subscribe/', kynect.views.subscribe),
    url(r'^account_portal/', kynect.views.account_portal),
    url(r'^user_devices/', kynect.views.user_devices),
    url(r'^track_location/', kynect.views.track_location),
    url(r'^update_location/(?P<device_id>\d+)/$', kynect.views.update_location, name="update_location"),
    url(r'^pet_details/', kynect.views.pet_details),
    url(r'^update_pet_details/(?P<pet_id>\d+)/$', kynect.views.update_pet_details, name='update_pet_details'),
    url(r'^pet_health/', kynect.views.pet_health),
    url(r'^notifications/', kynect.views.notifications),
    url(r'^delete_notifications/(?P<notification_id>\d+)/$', kynect.views.delete_notifications),
    url(r'^account_settings/', kynect.views.account_settings),
    url(r'^update_user_profile/', kynect.views.update_user_profile),
    url(r'^change_password/$', kynect.views.change_password, name="change_password"),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),                # Next 4 URLS are for PASSWORD RESET (USES AUTH VIEWS)
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', kynect.views.password_reset_complete, name='password_reset_complete'),
    url(r'^sign_up/$', kynect.views.sign_up, name='sign_up'),
    url(r'^account_activation_sent/$', kynect.views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate_account/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', kynect.views.activate_account, name='activate_account'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration_and_login/login.html', 'authentication_form': LoginForm}, name="login"),
    url(r'^logout/', auth_views.logout, {'next_page': '/home'}),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r'^debug/', include(debug_toolbar.urls)),
    ] + urlpatterns
