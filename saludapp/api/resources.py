from api.models import *
import requests
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.authentication import OAuthAuthentication
from tastypie.resources import ModelResource
from saludapp import auth0backend as auth0
from django.contrib.auth.decorators import login_required


class CitaResource(ModelResource):
    class Meta:

        queryset = Cita.objects.all()
        resource_name = 'cita'
        autentication=OAuthAuthentication()
        authorization = Authorization()
        fields = ['tipo', 'paciente']


class MedicoResource(ModelResource):
    class Meta:
        queryset = Medico.objects.all()
        resource_name = 'medico'

        def hydrate_id(self, bundle):
            bundle.data['id'] = auth0.user_id()
            return bundle

        autentication = OAuthAuthentication()
        authorization = Authorization()
        fields = ['cedula', 'nombre']


class PacienteResource(ModelResource):
    class Meta:
        queryset = Paciente.objects.all()
        resource_name = 'user'

        def hydrate_id(self, bundle):
            bundle.data['id'] = auth0.user_id()
            return bundle

        autentication = OAuthAuthentication()
        authorization = Authorization()
        fields = ['cedula', 'nombre']
