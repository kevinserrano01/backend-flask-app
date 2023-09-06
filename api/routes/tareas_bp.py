from flask import Blueprint
from api.controllers.tareasController import TareasController

tarea_bp = Blueprint('tarea_bp',  __name__)

@tarea_bp.route('/tareas', methods=['GET'])
def listar_tareas():
    return TareasController.get_tasks()

@tarea_bp.route('/tarea/<int:tarea_id>', methods=['GET'])
def obtener_tarea(tarea_id):
    return TareasController.get_task(tarea_id)

@tarea_bp.route('/eliminar_tarea/<int:tarea_id>')
def eliminar_tarea(tarea_id):
    return TareasController.delete_task(tarea_id)

@tarea_bp.route('/crear_tarea')
def crear_tarea():
    return TareasController.create_task()

@tarea_bp.route('/actualizar_tarea/<int:tarea_id>')
def actualizar_tarea(tarea_id):
    return TareasController.update_task(tarea_id)