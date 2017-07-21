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
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', kynect.views.home, name="home"),
    url(r'^home/', kynect.views.home),
    url(r'^features/', kynect.views.features),
    url(r'^about_us/', kynect.views.about_us),
    url(r'^subscribe/', kynect.views.subscribe),
    url(r'^profile/', kynect.views.profile),
    url(r'^track_location/', kynect.views.track_location),
    url(r'^sign_up/$', kynect.views.sign_up, name='sign_up'),
    url(r'^account_activation_sent/$', kynect.views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate_account/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', kynect.views.activate_account, name='activate_account'),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name="login"),
    url(r'^logout/', views.logout, {'next_page': '/home'}),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^debug/', include(debug_toolbar.urls)),
    ] + urlpatterns
