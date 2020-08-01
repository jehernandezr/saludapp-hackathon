from django.conf.urls import url, include
from django.urls import path
from api.resources import *
from tastypie.api import Api
from django.contrib import admin

v1_api = Api(api_name='v1')
v1_api.register(CitaResource())
v1_api.register(PacienteResource())
v1_api.register(MedicoResource())
v1_api.register(UserResource())
v1_api.register(DisponibleResource())


urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(v1_api.urls))

]
