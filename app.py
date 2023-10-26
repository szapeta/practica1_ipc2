from flask import jsonify, Flask, request
from flask_cors import CORS
import Pila

app = Flask(__name__)
CORS(app)

miPila = Pila.Pila()

@app.route('/addPila', methods=['POST'])     
def addPila():
    if request.method == 'POST':
        valorLeido = request.form['valor']
        miPila.insertar(valorLeido)
        return jsonify({"msg": "ok"})
    
#Generar endpoint para crear el grafo de la pila    
    
@app.route('/getPila')  
def getPila():
    return jsonify({"pila": miPila.printPila()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)