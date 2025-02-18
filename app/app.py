from flask import Flask
from app.controllers.problema_controller import problema_bp
from app.controllers.autor_controller import autor_bp
from app.controllers.static_controller import static_bp

def create_app():
    app = Flask(__name__)
    
    # Registrando os blueprints (controladores)
    app.register_blueprint(problema_bp)
    app.register_blueprint(autor_bp)
    app.register_blueprint(static_bp)

    return app
