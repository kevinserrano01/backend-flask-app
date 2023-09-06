class Tareas:
    def __init__(self, id_tarea, nombre, fecha_creacion, fecha_limite, completado,categoria, sub_tarea):
        self.id_tarea = id_tarea
        self.nombre=nombre
        self.fecha_creacion=fecha_creacion
        self.fecha_limite=fecha_limite
        self.completada=completado
        self.categoria = categoria
        self.sub_tarea = sub_tarea
        
    def __str__(self):
        return f"id: {self.id_tarea}, Nombre: {self.nombre}, f_creacion: {self.fecha_creacion}, f_limite: {self.fecha_limite}, completada: {self.completada}, categoria: {self.categoria}"

class Categorias:
    def __init__(self, id_categoria: int, nombre: str, descripcion: str):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self) -> str:
        return self.nombre

class Items:
    def __init__(self, id_item: int, detalle: str, completado: bool):
        self.id_item = id_item
        self.detalle = detalle
        self.completado = completado

    def __str__(self) -> str:
        return self.detalle

# Test
# limpieza = Categorias(2, 'limpieza', 'tareas de limpieza')
# sub_tarea1 = Items(3, 'Tender la cama', True)
# tarea1 = Tareas(1, 'limpiar Casa', '04/09/2023', '04/10/2023', False , limpieza, sub_tarea1)

# print(tarea1)