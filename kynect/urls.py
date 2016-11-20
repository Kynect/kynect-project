from django.conf.urls import url

from . import views

app_name = 'kynect'
urlpatterns = [
	# ex: /kynect/
    url(r'', views.index, name='index'),
]