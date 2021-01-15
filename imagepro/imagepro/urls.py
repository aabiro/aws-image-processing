from django.conf.urls import include, url
from myapp.views import home, process 

urlpatterns = [
    url(r'^$', home, name='home'),	
    url(r'^process/$', process, name='process'),
]


