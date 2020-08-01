from builtins import print

import simplejson as simplejson
from api.models import *
from django.db import IntegrityError
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication,BasicAuthentication
from tastypie.exceptions import BadRequest
from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tastypie.http import HttpUnauthorized, HttpForbidden
from django.conf.urls import url
from tastypie.utils import trailing_slash
from tastypie.authorization import DjangoAuthorization


class CitaResource(ModelResource):
    user = fields.ForeignKey('api.resources.UserResource', attribute='user', related_name='user', full=True)
    class Meta:
        queryset = Cita.objects.all()
        resource_name = 'cita'
        autentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        fields = ['tipo', 'paciente']


class MedicoResource(ModelResource):
    user = fields.ForeignKey('api.resources.UserResource', attribute='user', related_name='user', full=True)

    class Meta:
        queryset = Medico.objects.all()
        resource_name = 'medico'

        autentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        fields = ['cedula', 'nombre']


class PacienteResource(ModelResource):


    class Meta:
        queryset = Paciente.objects.all()
        resource_name = 'paciente'
        autentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        fields = ['cedula', 'nombre']


class UserResource(ModelResource):
    class Meta:
        object_class = User
        queryset = User.objects.all()
        fields = ['username', 'first_name', 'last_name', 'email']
        allowed_methods = ['post']
        resource_name = 'user'
        include_resource_uri = False
        authentication = Authentication()
        always_return_data = True
        excludes = ['email', 'password', 'is_superuser']
        authorization = Authorization()

    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('login'), name="api_login"),
            url(r'^(?P<resource_name>%s)/logout%s$' %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('logout'), name='api_logout')
        ]

    def obj_create(self, bundle, request=None, **kwargs):
        try:
            bundle = super(UserResource, self).obj_create(bundle, request=request, **kwargs)
            bundle.obj.set_password(bundle.data.get('password'))
            bundle.obj.save()

        except IntegrityError:
            raise BadRequest('User with this username already exists')

        return bundle

    def login(self, request=None, **kwargs):
        self.method_check(request, allowed=['post'])

        data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))

        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return self.create_response(request, {
                    'success': True
                })
            else:
                return self.create_response(request, {
                    'success': False,
                    'reason': 'disabled',
                }, HttpForbidden)
        else:
            return self.create_response(request, {
                'success': False,
                'reason': 'incorrect',
            }, HttpUnauthorized)

    def logout(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        if request.user and request.user.is_authenticated:
            logout(request)
            return self.create_response(request, { 'success': True })
        else:
            return self.create_response(request, { 'success': False }, HttpUnauthorized)


class DisponibleResource(ModelResource):
    class Meta:
        queryset = Disponible.objects.all()
        resource_name = 'disponible'
        autentication = Authentication()
        authorization = Authorization()
        fields = ['medico', 'fecha', 'tipo']



