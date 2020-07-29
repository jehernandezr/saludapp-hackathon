from ..models import *
import datetime
from twilio.rest import Client

def createCita(cedula,fecha, hora):
    
    usuario = Paciente.objects.get(cedula=cedula)
    fecha = fecha+' '+hora
    format = '%Y-%d-%m %H:%M'
    datetime_str = datetime.datetime.strptime(fecha, format)

    cita = Disponible.objects.filter(fecha=fecha).filter(estado='L')
    if cita and usuario:
        medico = cita[0].medico
        reserva = Cita(medico=medico,paciente=usuario,disponible=cita[0])
        sendSMS(reserva.url,usuario.celular,fecha,hora)
        reserva.save()
        return True
    return False

def sendSMS(link, celular, dia, hora):
    account_sid = 'ACcc467e48ab7f253e2de98eca1667ad16'
    auth_token = '1d8e51c2405c99fb74055ad7fdf0513b'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Su cita ha sido confirmada para el día {dia} a las {hora}. El link para acceder a ella es: {link}',
        from_='+17252139009',
        to='+57'+celular
    )
