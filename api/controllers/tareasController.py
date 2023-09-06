from api.database import *
from flask import request

class TareasController:
    
    @classmethod
    def get_tasks(self):
        sql = "SELECT * FROM tareas"
        resultado = DatabaseConnection.fetch_all(sql)
        lista_tareas = []
        if resultado is not None:
            for tarea in resultado:
                lista_tareas.append({
                    "tarea_id": tarea[0],
                    "nombre": tarea[1],
                    "fecha_creacion": tarea[2],
                    "fecha_limite": tarea[3],
                    "comletada": tarea[4],
                    "subtarea": tarea[5],
                    "categoria_id": tarea[6]
                })
        return lista_tareas
    
    @classmethod
    def get_task(self, tarea_id):
        sql = "SELECT * FROM tareas WHERE id_tarea = %s"
        params = tarea_id,
        resultado = DatabaseConnection.fetch_one(sql, params)
        if resultado is not None:
            return {
                "tarea_id": resultado[0],
                    "nombre": resultado[1],
                    "fecha_creacion": resultado[2],
                    "fecha_limite": resultado[3],
                    "comletada": resultado[4],
                    "subtarea": resultado[5],
                    "categoria_id": resultado[6]
            }, 200
        return {"msg": "No se encontró la tarea"}, 404
    
    @classmethod
    def delete_task(self, tarea_id):
        sql = "DELETE FROM todo_app.tareas WHERE id_tarea = %s"
        params = tarea_id,
        DatabaseConnection.execute_query(sql, params)
        return {"msg": f"La tarea con id: {tarea_id} fue eliminado"}, 204
    
    @classmethod
    def create_task(self):
        nombre = request.args.get('nombre')
        fecha_limite = request.args.get('fecha_limite')
        completada = request.args.get('completada')
        subtarea = request.args.get('subtarea')
        id_categoria = request.args.get('id_categoria')

        sql = """INSERT INTO tareas (nombre, fecha_limite, completada, subtarea, id_categoria)
                VALUES (%s, %s, %s, %s, %s);
            """
        params = nombre, fecha_limite, completada, subtarea, id_categoria,
        DatabaseConnection.execute_query(sql, params)
        datos = {
            "nombre": nombre,
            "fecha_limite": fecha_limite,
            "completada": completada,
            "subtarea": subtarea,
            "id_categoria": id_categoria
        }
        return datos, 201
    
    @classmethod
    def update_task(self, tarea_id):
        nombre = request.args.get('nombre')
        fecha_limite = request.args.get('fecha_limite')
        sql = "UPDATE tareas SET nombre = %s, fecha_limite = %s WHERE id_tarea = %s"
        params = nombre, fecha_limite, tarea_id,
        DatabaseConnection.execute_query(sql, params)
        return {"msg": f"La tarea con id: {tarea_id} fue Actualizada"}, 200


# CRUD = CREATE, READ, UPDATE, DELETE