
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	
	#url(r'^video/$', views.screenshot, name='video'),
    url(r'^$', views.index, name='index'),
    
   
   
)