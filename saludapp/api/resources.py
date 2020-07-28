from api.models import *
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.authentication import Authentication, BasicAuthentication
from tastypie.resources import ModelResource
from ..saludapp import auth0backend as auth0
from django.contrib.auth.decorators import login_required


class CitaResource(ModelResource):
    class Meta:
        queryset = Cita.objects.all()
        resource_name = 'cita'
        authorization = Authorization()
        fields = ['tipo', 'paciente']


class MedicoResource(ModelResource):
    class Meta:
        queryset = Medico.objects.all()
        resource_name = 'medico'
        authorization = Authorization()
        fields = ['cedula', 'nombre']


class PacienteResource(ModelResource):
    class Meta:
        queryset = Paciente.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        fields = ['cedula', 'nombre']



