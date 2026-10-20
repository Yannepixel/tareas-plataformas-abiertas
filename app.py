from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/estudiantes/api/v1/hola', methods=['GET'])
def hola():
    return "hola mundo"

@app.route('/estudiantes/api/v1/saludo', methods=['GET'])
def saludo():
    data = request.get_json(silent=True) or {}
    
    nombre = data.get('nombre') or request.args.get('nombre')
    apellido = data.get('apellido') or request.args.get('apellido')

    if not nombre:
        return "Debe de ingresar el nombre del estudiante.", 400

    nombre_completo = f"{nombre} {apellido}" if apellido else nombre
    return jsonify({"saludo": f"Hola {nombre_completo}"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)