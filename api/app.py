from flask import Flask
from api.routes.tareas_bp import tarea_bp
from api.routes.categorias_bp import categoria_bp

app = Flask(__name__)

# Registrar BluPrint
app.register_blueprint(tarea_bp)
app.register_blueprint(categoria_bp)