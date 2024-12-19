 # routes/categoria_routes.py
from flask import Blueprint,  request
from controllers.categoriaController import CategoriaController

# Creamos un Blueprint para las rutas de categoria
categoria_bp = Blueprint('categoria_bp', __name__)

# Ruta para obtener todas las categorías
@categoria_bp.route('/categorias', methods=['GET'])
def obtener_categorias():
    return CategoriaController.obtener_todas_categorias()

# Ruta para obtener una categoría por id
@categoria_bp.route('/categoria/<int:id_categoria>', methods=['GET'])
def obtener_categoria(id_categoria):
    return CategoriaController.obtener_categoria_por_id(id_categoria)

# Ruta para agregar una nueva categoría
@categoria_bp.route('/categoria', methods=['POST'])
def agregar_categoria():
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return CategoriaController.agregar_categoria(data)

# Ruta para actualizar una categoría
@categoria_bp.route('/categoria/<int:id_categoria>', methods=['PUT'])
def actualizar_categoria(id_categoria):
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return CategoriaController.actualizar_categoria(id_categoria, data)

# Ruta para eliminar una categoría
@categoria_bp.route('/categoria/<int:id_categoria>', methods=['DELETE'])
def eliminar_categoria(id_categoria):
    return CategoriaController.eliminar_categoria(id_categoria)