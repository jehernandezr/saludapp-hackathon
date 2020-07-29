from django.conf.urls import url, include
from django.urls import path
from api.resources import *
from tastypie.api import Api
from django.contrib import admin
from  api import  views
from django.contrib.auth.decorators import login_required
from . import auth0backend as auth

v1_api = Api(api_name='v1')
v1_api.register(CitaResource())
v1_api.register(PacienteResource())
v1_api.register(MedicoResource())
v1_api.wrap_view(views)


urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
    path('autenticado/', views.redirigir, name='redirect'),
]
