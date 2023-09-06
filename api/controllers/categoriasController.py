from api.database import *
from flask import request

class CategoriasController:

    @classmethod
    def get_categories(self):
        sql = "SELECT * FROM categorias"
        resultado = DatabaseConnection.fetch_all(sql)
        lista_categorias = []
        if resultado is not None:
            for categoria in resultado:
                lista_categorias.append({
                    "id_categoria": categoria[0],
                    "nombre": categoria[1],
                    "descripcion": categoria[2],
                })
        return lista_categorias

    @classmethod
    def get_categoria(self, categoria_id):
        sql = "SELECT * FROM categorias WHERE id_categoria = %s"
        params = categoria_id,
        resultado = DatabaseConnection.fetch_one(sql, params)
        if resultado is not None:
            return {
                "categoria_id": resultado[0],
                    "nombre": resultado[1],
                    "descripcion": resultado[2],
                    
            }, 200
        return {"msg": "No se encontró la tarea"}, 404

    @classmethod
    def delete_categoria(self, categoria_id):
        sql = "DELETE FROM todo_app.categorias WHERE id_categoria = %s"
        params = categoria_id,
        DatabaseConnection.execute_query(sql, params)
        return {"msg": f"La categoria con id: {categoia_id} fue eliminada"}, 204

    @classmethod
    def create_category(self):
        nombre = request.args.get('nombre')
        descripcion = request.args.get('descripcion')

        sql = """INSERT INTO categorias (nombre, descripcion)
                VALUES (%s, %s);
            """
        params = nombre, descripcion
        DatabaseConnection.execute_query(sql, params)
        datos = {
            "nombre": nombre,
            "descripcion": descripcion,
        }
        return datos, 201

    @classmethod
    def update_categoria(self, categoria_id):
        nombre = request.args.get('nombre')
        descripcion = request.args.get('descripcion')
        sql = "UPDATE categorias SET nombre = %s, descripcion = %s WHERE id_categoria = %s"
        params = nombre, descripcion,
        DatabaseConnection.execute_query(sql, params)
        return {"msg": f"La categoria con id: {categoria_id} fue Actualizada"}, 200


# Campos de tabla categorias: id_categoria, nombre, descripcion