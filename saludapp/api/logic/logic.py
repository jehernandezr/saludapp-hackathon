from ..models import *
import datetime
def createCita(cedula,fecha, hora):


    usuario = Paciente.objects.get(cedula=cedula)
    fecha = fecha+' '+hora
    format = '%Y-%d-%m %H:%M'
    datetime_str = datetime.datetime.strptime(fecha, format)

    cita = Disponible.objects.filter(fecha=fecha).filter(estado='L')
    if cita and usuario:
        medico = cita[0].medico
        reserva = Cita(medico=medico,paciente=usuario,disponible=cita[0])
        reserva.save()
        return True
    return False
