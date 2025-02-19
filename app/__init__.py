# app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Aqui você pode registrar controladores (blueprints) e outras configurações
    from app.controllers.problema_controller import problema_bp
    app.register_blueprint(problema_bp)

    return app