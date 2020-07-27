from tastypie.resources import ModelResource
from api.models import *
from tastypie.authorization import Authorization
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

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        fields = ['cedula', 'nombre']