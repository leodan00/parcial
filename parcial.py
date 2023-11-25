
from flask import Flask, jsonify, request

app = Flask(__name__)



# Datos de ejemplo (simulando una base de datos)
usuarios = [
    {'id': 1, 'nombre': 'Usuario1', 'edad': 25},
    {'id': 2, 'nombre': 'Usuario2', 'edad': 30},
    {'id': 3, 'nombre': 'Usuario3', 'edad': 27}
]

# Ruta para obtener todos los usuarios
@app.route('/', methods=['GET'])
def obtener_usuarios():
    return jsonify({'usuarios': usuarios})

# Ruta para obtener un usuario por su ID
@app.route('/usuario/<int:user_id>', methods=['GET'])
def obtener_usuario(user_id):
    usuario = next((usuario for usuario in usuarios if usuario['id'] == user_id), None)
    if usuario:
        return jsonify({'usuario': usuario})
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404

# Ruta para agregar un nuevo usuario
@app.route('/usuario', methods=['POST'])
def agregar_usuario():
    nuevo_usuario = request.json
    if not nuevo_usuario or 'id' not in nuevo_usuario or 'nombre' not in nuevo_usuario or 'edad' not in nuevo_usuario:
        return jsonify({'mensaje': 'Datos incompletos para agregar un usuario'}), 400
    
    usuarios.append(nuevo_usuario)
    return jsonify({'mensaje': 'Usuario agregado correctamente'})























if __name__ == '__main__':
    app.run(debug=True)


