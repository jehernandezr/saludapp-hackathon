from django.shortcuts import render
from saludapp import auth0backend as auth
from django.contrib.auth.decorators import login_required
from .resources import *

@login_required
def redirigir(request):
    role = auth.getRole(request)
    if role == 'Medico':
        return MedicoResource()
    elif role == 'Paciente':
        return PacienteResource()

