from flask import Flask
from flask import send_file,jsonify, request
import json
import os
import sys
project_home = str(os.path.abspath(os.getcwd())).replace("""\ """.replace(" ",""),"/").replace("/api/bot","")
print(project_home)
if project_home not in sys.path:
    sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'saludapp.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from api.logic.logic import *

app = Flask(__name__)

@app.route('/dynamicsay', methods=['POST'])
def dynamic_say():
    return send_file('dynamicsay.json')

@app.route('/collect',  methods=['POST'])
def collect():
    memory = json.loads(request.form.get('Memory'))

    answers = memory['twilio']['collected_data']['reserva']['answers']

    cedula = answers['cedula']['answer']
    dia = answers['dia']['answer']
    hora = answers['hora']['answer']

    guardar = createCita(cedula,dia,hora)
    if guardar:
        message = (
            f'Bien!, he podido reservar la cita al siguiente número de documento {cedula}.'
            f' El día de la cita es {dia} a la(s) {hora}.'
            f'No faltes!'
        )
    else:
        message = ('No se pudo guardar la cita')

    return jsonify(actions=[{'say': {'speech': message}}])

if __name__ == "__main__":
    app.run()
