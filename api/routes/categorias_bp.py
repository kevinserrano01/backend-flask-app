from flask import Blueprint
from api.controllers.categoriasController import CategoriasController

categoria_bp = Blueprint('categoria_bp', __name__)

@categoria_bp.route('/categorias', methods = ['GET'])
def listar_categorias():
    return CategoriasController.get_categories()

@categoria_bp.route('/categoria/<int:categoria_id>', methods=['GET'])
def obtener_categoria(categoria_id):
    return CategoriasController.get_categoria(categoria_id)

@categoria_bp.route('/eliminar_categoria/<int:categoria_id>')
def eliminar_categoria(categoria_id):
    return CategoriasController.delete_categoria(categoria_id)

@categoria_bp.route('/crear_categoria')
def crear_categoria():
    return CategoriasController.create_category()

@categoria_bp.route('/actualizar_categoria/<int:categoria_id>')
def actualizar_categoria(categoria_id):
    return CategoriasController.update_categoria(categoria_id)