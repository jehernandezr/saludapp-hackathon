from twilio.rest import Client
def sendSMS(link,celular, dia,hora):
    account_sid = 'ACcc467e48ab7f253e2de98eca1667ad16'
    auth_token = '1d8e51c2405c99fb74055ad7fdf0513b'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Su cita ha sido confirmada para el día {dia} a las {hora}. El link para acceder a ella es: {link}',
        from_='+17252139009',
        to='+57'+celular
    )

sendSMS("www.google.com", "3138864366", '9-12-2000', '18:00')
