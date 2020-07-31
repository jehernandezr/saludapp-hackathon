from ..models import *
import datetime
from twilio.rest import Client
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import qrcode
import os
from email import encoders
from email.mime.base import MIMEBase

def createCita(cedula,fecha, hora):

    usuario = Paciente.objects.get(cedula=cedula)
    fecha = fecha+' '+hora
    format = '%Y-%m-%d %H:%M'
    datetime_str = datetime.datetime.strptime(fecha, format)
    cita = Disponible.objects.filter(fecha=datetime_str).filter(estado='L')
    if cita and usuario:
        medico = cita[0].medico

        reserva = Cita(medico=medico,paciente=usuario,disponible=cita[0])
        setattr(cita[0], 'estado', 'R')
        cita[0].save()
        sendSMS(reserva.url,usuario.celular,fecha,hora)
        sendMail(reserva.url,usuario,fecha,hora)
        reserva.save()
        return True
    return False

def sendSMS(link, celular, dia, hora):
    account_sid = 'ACcc467e48ab7f253e2de98eca1667ad16'
    auth_token = '1d8e51c2405c99fb74055ad7fdf0513b'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Tu cita ha sido confirmada para el día {dia} a las {hora}. El link para acceder a ella es: {link}',
        from_='+17252139009',
        to='+57'+celular
    )

def sendMail(link,usuario,dia,hora):

    img = qrcode.make(link)
    ruta_imagen = f'{usuario.cedula}.png'
    img.save(ruta_imagen)

    sender_email = "aippointment@gmail.com"
    receiver_email = usuario.correo
    password = "HackathonUniandes2020"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Confirmación cita"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    html = f"""\
    <html>
      <body>
        <p>Hola {usuario.nombre},<br>
           Tu cita ha sido confirmada para el día {dia} a las {hora}.,<br>
           <a href="{link}">Haz click aquí para acceder a tu cita.</a>
        </p>
        <p> O escanea el código QR adjunto para acceder a tu cita.
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, "html")
    # Open PDF file in binary mode
    with open(ruta_imagen, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {ruta_imagen}",
    )

    message.attach(part)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    os.remove(ruta_imagen)