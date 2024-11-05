from flask import Flask,jsonify, request
import requests
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/get_data', methods=['GET'])
def get_data():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
    data = response.json()  # Convierte la respuesta en JSON
    return jsonify(data)
if __name__ == '__main__':
    app.run()
