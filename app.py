from flask import Flask, request, jsonify

app = Flask(__name__)

# ========== ENDPOINTS DE LA PRÁCTICA ANTERIOR ==========

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


# ========== NUEVOS ENDPOINTS - PRÁCTICA 3 ==========

# 1. Obtener todos los estudiantes
@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    return jsonify({
        "mensaje": "Lista de estudiantes obtenida correctamente.",
        "estudiantes": [
            "Ana",
            "Carlos",
            "María"
        ]
    })

# 2. Agregar un estudiante
@app.route('/estudiantes', methods=['POST'])
def agregar_estudiante():
    data = request.get_json()
    nombre = data.get('nombre')
    
    return jsonify({
        "mensaje": "Estudiante agregado correctamente.",
        "estudiante": nombre
    })

# 3. Actualizar un estudiante
@app.route('/estudiantes/<int:id>', methods=['PUT'])
def actualizar_estudiante(id):
    data = request.get_json()
    nombre = data.get('nombre')
    
    return jsonify({
        "mensaje": "Estudiante actualizado correctamente.",
        "id": id
    })

# 4. Eliminar un estudiante
@app.route('/estudiantes/<int:id>', methods=['DELETE'])
def eliminar_estudiante(id):
    return jsonify({
        "mensaje": "Estudiante eliminado correctamente.",
        "id": id
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
