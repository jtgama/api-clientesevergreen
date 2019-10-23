from flask import Flask, jsonify, request, render_template
import requests
app = Flask(__name__, template_folder="templates")

actividades_list = ['Agricultura','Comercio', 'Invetigacion', 'Insumo','Transporte']

@app.route('/listarparticipante', methods = ['GET'])
def listarparticipante():
    participan_list = requests.get('https://api-client-evergreen-134.azurewebsites.net/participant').json()
    return render_template('listarparticipante.html', participan = participan_list)

@app.route('/ingreparticipa', methods = ['GET'])
def NewCultivo():
    return render_template('nuevoParticipa.html', variables = actividades_list)

@app.route('/guardarparticipante', methods=['POST'])
def saveCultivo():
   participantes = dict(request.values)
   
    participantes['estrato'] = int(participantes['estrato'])
   requests.post('https://api-client-evergreen-134.azurewebsites.net/participant', json=participantes)
   return(listarparticipante())